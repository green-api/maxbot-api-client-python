import asyncio, httpx, logging, time, threading
from functools import wraps
from typing import Any, TypeVar, Type
from urllib.parse import urljoin

from maxbot_api_client_python.exceptions import build_api_error
from maxbot_api_client_python.types.models import Config

logger = logging.getLogger(__name__)

T = TypeVar('T')
class Client:
    def __init__(self, cfg: Config):
        if not cfg.base_url or not cfg.token:
            raise ValueError("base_url and token must be set")

        self.base_url = cfg.base_url.rstrip("/") + "/"
        self.token = cfg.token

        self.timeout = cfg.timeout if cfg.timeout > 0 else 35
        self.max_retries = cfg.max_retries
        self.retry_delay_sec = cfg.retry_delay_sec

        rps = cfg.ratelimiter if cfg.ratelimiter > 0 else 25
        self._limiter_interval = 1.0 / rps if rps > 0 else 0.0
        self._sync_lock = threading.Lock()
        self._async_lock: asyncio.Lock | None = None
        self._last_request_time = 0.0

        self.headers = {"Authorization": self.token}

        self._sync_client = httpx.Client(timeout=self.timeout)
        self._async_client: httpx.AsyncClient | None = None

    def _get_delay(self) -> float:
        if self._limiter_interval <= 0:
            return 0.0
        now = time.monotonic()
        elapsed = now - self._last_request_time
        delay = max(0.0, self._limiter_interval - elapsed)
        self._last_request_time = now + delay
        return delay

    def _wait_limit(self) -> None:
        if self._limiter_interval <= 0:
            return
        with self._sync_lock:
            delay = self._get_delay()
        if delay > 0:
            time.sleep(delay)

    async def _await_limit(self) -> None:
        if self._limiter_interval <= 0:
            return
        if self._async_lock is None:
            self._async_lock = asyncio.Lock()
        async with self._async_lock:
            delay = self._get_delay()
        if delay > 0:
            await asyncio.sleep(delay)

    def __enter__(self) -> "Client":
        return self
        
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()

    async def __aenter__(self) -> "Client":
        return self
        
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        await self.aclose()

    async def get_async_client(self) -> httpx.AsyncClient:
        if self._async_client is None:
            self._async_client = httpx.AsyncClient(timeout=self.timeout)
        return self._async_client

    def close(self) -> None:
        self._sync_client.close()

    async def aclose(self) -> None:
        if self._async_client:
            await self._async_client.aclose()
            self._async_client = None

    def _build_url(self, path: str) -> str:
        if path.startswith(("http://", "https://")):
            return path
        return urljoin(self.base_url, path.lstrip("/"))

    def _prepare_data(self, payload: Any) -> Any:
        if hasattr(payload, "model_dump"):
            return payload.model_dump(exclude_none=True)
        return payload

    def split_request(self, req: Any) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
        if not hasattr(req, "model_fields"):
            return None, self._prepare_data(req)
            
        data = req.model_dump(exclude_none=True, by_alias=True)
        query, payload = {}, {}
        
        for field_name, field in req.model_fields.items():
            key = field.alias or field_name
            if key not in data:
                continue
                
            extra = field.json_schema_extra
            extra_dict = extra if isinstance(extra, dict) else {}
            
            if extra_dict.get("in_path"):
                continue
            elif extra_dict.get("in_query"):
                query[key] = data[key]
            else:
                payload[key] = data[key]
                
        return (query if query else None, payload if payload else None)

    def request(
        self, 
        method: str, 
        path: str, 
        query: dict[str, Any] | None = None, 
        payload: Any = None, 
        files: dict[str, Any] | None = None
    ) -> bytes:
        self._wait_limit()
        
        headers = self.headers.copy()
        if not files:
            headers["Content-Type"] = "application/json"

        response = self._sync_client.request(
            method=method,
            url=self._build_url(path),
            params=query,
            json=self._prepare_data(payload) if not files else None,
            data=None if not files else payload,
            files=files,
            headers=headers
        )
        return self._handle_response(response)

    async def arequest(
        self, 
        method: str, 
        path: str, 
        query: dict[str, Any] | None = None, 
        payload: Any = None, 
        files: dict[str, Any] | None = None
    ) -> bytes:
        await self._await_limit()
        
        api = await self.get_async_client()
        headers = self.headers.copy()
        if not files:
            headers["Content-Type"] = "application/json"

        response = await api.request(
            method=method,
            url=self._build_url(path),
            params=query,
            json=self._prepare_data(payload) if not files else None,
            data=None if not files else payload,
            files=files,
            headers=headers
        )
        return self._handle_response(response)

    def _handle_response(self, response: httpx.Response) -> bytes:
        if not (200 <= response.status_code < 300):
            raise build_api_error(response)
        return response.content
    
    def _parse_response(self, data: bytes, model_class: Type[T]) -> T:
        if not data or data.strip() in (b"", b"<retval>1</retval>"):
            return model_class.model_construct()
        try:
            return model_class.model_validate_json(data)
        except Exception as e:
            logger.error(f"Server returned invalid response. Size: {len(data)} bytes.")
            failed_response = httpx.Response(status_code=500, content=data, request=httpx.Request("GET", self.base_url))
            raise build_api_error(failed_response) from e
    
    def decode(self, method: str, path: str, model_class: type[T], **kwargs: Any) -> T:
        response = self.request(method, path, **kwargs)
        return self._parse_response(response, model_class)

    async def adecode(self, method: str, path: str, model_class: type[T], **kwargs: Any) -> T:
        response = await self.arequest(method, path, **kwargs)
        return self._parse_response(response, model_class)