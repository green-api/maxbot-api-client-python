import time, json, asyncio, httpx, threading, logging
from functools import wraps
from urllib.parse import urljoin
from .exceptions import HandleErrorResponse
from typing import Optional, Dict, Any, Type, TypeVar

T = TypeVar("T")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger("httpx").setLevel(logging.WARNING)
log = logging.getLogger(__name__)

class RateLimiter:
    def __init__(self, rps: int):
        self._lock = threading.Lock()
        self._alock = asyncio.Lock()
        self.last_request_time = 0.0
        self.set_limit(rps)

    def set_limit(self, rps: int):
        self.limit = rps
        self.interval = 1.0 / rps if rps > 0 else 0

    def wait(self):
        if self.interval <= 0:
            return

        with self._lock:
            now = time.time()
            elapsed = now - self.last_request_time
            delay = max(0.0, self.interval - elapsed)
            self.last_request_time = now + delay 
            
        if delay > 0:
            time.sleep(delay)

    async def async_wait(self):
        if self.interval <= 0:
            return

        async with self._alock:
            now = time.time()
            elapsed = now - self.last_request_time
            delay = max(0.0, self.interval - elapsed)
            self.last_request_time = now + delay
            
        if delay > 0:
            await asyncio.sleep(delay)

class Config:
    def __init__(self, base_url: str, token: str, timeout: int = 35, ratelimiter: int = 25, max_retries: int = 3, retry_delay_sec: int = 3):
        self.base_url = base_url
        self.token = token
        self.timeout = timeout
        self.ratelimiter = ratelimiter
        self.max_retries = max_retries
        self.retry_delay_sec = retry_delay_sec

class Client:
    def __init__(self, cfg: Config):
        if not cfg.base_url or not cfg.token:
            raise ValueError("BaseURL and Token must be set")

        self.base_url = cfg.base_url.rstrip("/") + "/"
        self.token = cfg.token

        self.timeout = cfg.timeout if cfg.timeout > 0 else 35
        self.global_limiter = RateLimiter(cfg.ratelimiter if cfg.ratelimiter > 0 else 25)
        self.max_retries = cfg.max_retries
        self.retry_delay_sec = cfg.retry_delay_sec

        self.headers = {"Authorization": self.token}

        self._sync_client = httpx.Client(timeout=self.timeout)
        self._async_client: Optional[httpx.AsyncClient] = None

    async def get_async_client(self) -> httpx.AsyncClient:
        if self._async_client is None:
            self._async_client = httpx.AsyncClient(timeout=self.timeout)
        return self._async_client

    def close(self):
        self._sync_client.close()

    async def aclose(self):
        if self._async_client:
            await self._async_client.aclose()

    def _build_url(self, path: str) -> str:
        if path.startswith(("http://", "https://")):
            return path
        return urljoin(self.base_url, path.lstrip("/"))

    def _prepare_data(self, payload: Any):
        if hasattr(payload, "model_dump"):
            return payload.model_dump(exclude_none=True)
        return payload

    def request(self, method: str, path: str, query: Optional[Dict] = None, payload: Any = None, files: Optional[Dict] = None) -> bytes:
        self.global_limiter.wait()
        
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
        log.debug(f"Response body: {response.text}")
        return self._handle_response(response)

    async def arequest(self, method: str, path: str, query: Optional[Dict] = None, payload: Any = None, files: Optional[Dict] = None) -> bytes:
        await self.global_limiter.async_wait()
        
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
        log.debug(f"Response body: {response.text}")
        return self._handle_response(response)

    def _handle_response(self, response: httpx.Response) -> bytes:
        if not (200 <= response.status_code < 300):
            raise HandleErrorResponse(response, response.content)
        return response.content
    
    def _parse_response[T](self, data: bytes, model_class: Type[T]) -> T:
        if not data or data.strip() == b"":
            return model_class()
        if data.strip() == b'<retval>1</retval>':
            return model_class()
        try:
            parsed_json = json.loads(data)
        except json.JSONDecodeError:
            log.error(f"Server returned non-JSON response: {data[:100]}")
            return model_class()

        if hasattr(model_class, "model_validate"):
            return model_class.model_validate(parsed_json)
        return parsed_json
    
def decode[T](client: Client, method: str, path: str, model_class: Type[T], **kwargs) -> T:
    response = client.request(method, path, **kwargs)
    return client._parse_response(response, model_class)

async def adecode[T](client: Client, method: str, path: str, model_class: Type[T], **kwargs) -> T:
    response = await client.arequest(method, path, **kwargs)
    return client._parse_response(response, model_class)

def as_async(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        return await asyncio.to_thread(func, *args, **kwargs)
    return wrapper