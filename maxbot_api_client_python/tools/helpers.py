import aiofiles, asyncio, httpx, logging, mimetypes, os, tempfile, time, re
from typing import Any, List, Optional
from urllib.parse import urlparse
from pathlib import Path

from maxbot_api_client_python.exceptions import MaxBotError
from maxbot_api_client_python.tools.uploads import Uploads
from maxbot_api_client_python.client import Client
from maxbot_api_client_python.types.constants import AttachmentType, Paths, UploadType
from maxbot_api_client_python.types.models import Message, SendFileReq, SendMessageReq, UploadFileReq, Attachment

logger = logging.getLogger(__name__)

class Helpers:
    def __init__(self, client: Client):
        self.client = client
        self.uploads = Uploads(client)

    def send_file(self, req: SendFileReq) -> Optional[Message]:
        """
        A helper that simplifies sending files to a chat.
        It automatically determines whether the provided file_source is a direct URL or a local file path.

        Example:
            # Sending a file via URL:
            response = bot.helpers.send_file(SendFileReq(
                chat_id=123456789,
                text="Check out this image!",
                file_source="https://example.com/image.png"
            ))

            # Sending a local file:
            response = bot.helpers.send_file(SendFileReq(
                chat_id=123456789,
                text="Here is the report.",
                file_source="/local/path/to/report.pdf"
            ))
        """
        is_url = urlparse(req.file_source).scheme in ("http", "https")
        if not is_url and not os.path.exists(req.file_source):
            raise ValueError("Invalid file path or URL.")
        
        if urlparse(req.file_source).scheme in ("http", "https"):
            return self._send_file_by_url(req)
            
        return self._send_file_by_upload(req)

    def _send_file_by_url(self, req: SendFileReq) -> Optional[Message]:
        ext = self._get_extension(req.file_source)
        upload_type = self._determine_upload_type(ext)

        if upload_type == UploadType.IMAGE:
            attachment = Attachment(type=AttachmentType.IMAGE, payload={"url": req.file_source})
            return self._send_file_internal(req, attachment)

        temp_path = None
        try:
            temp_path = self._download_temp_file(req.file_source)
            req_copy = req.model_copy(update={"file_source": temp_path})
            return self._send_file_by_upload(req_copy)
        except Exception as e:
            logger.error(f"File processing/upload error: {e}")
            raise
        finally:
            if temp_path:
                try:
                    os.remove(temp_path)
                except FileNotFoundError:
                    pass

    def _send_file_by_upload(self, req: SendFileReq) -> Optional[Message]:
        ext = self._get_extension(req.file_source)
        upload_type = self._determine_upload_type(ext)

        upload_req = UploadFileReq(type=upload_type, file_path=req.file_source)
        upload_resp = self.uploads.upload_file(upload_req)

        if not upload_resp or not upload_resp.token:
            logger.error("Upload failed: No token returned.")
            return None

        attachment = self._build_attachment_from_token(upload_type, upload_resp.token, Path(req.file_source).name)
        return self._send_file_internal(req, attachment)

    def _send_file_internal(self, req: SendFileReq, attachment: Attachment) -> Message:
        attachments: List[Attachment] = req.attachments or []
        attachments.append(attachment)

        request_data = SendMessageReq(
            user_id=req.user_id,
            chat_id=req.chat_id,
            text=req.text,
            format=req.format,
            attachments=attachments,
            notify=req.notify,
            link=req.link,
            disable_link_preview=req.disable_link_preview
        )

        query, payload = self.client.split_request(request_data)
        last_err: Optional[Exception] = None
        
        for _ in range(self.client.max_retries):
            try:
                return self.client.decode("POST", Paths.MESSAGES, Message, query=query, payload=payload)
            except MaxBotError as e:
                last_err = e
                if e.status_code == 422 or "not.ready" in str(e.response).lower():
                    time.sleep(self.client.retry_delay_sec)
                    continue
                break

        if last_err:
            raise last_err
        raise Exception("Unknown error in sendFileInternal")

    async def send_file_async(self, req: SendFileReq) -> Optional[Message]:
        """
        Async version of send_file.

        Example:
        # Sending a local file asynchronously:
        response = await bot.helpers.send_file_async(SendFileReq(
            chat_id=123456789,
            text="Here is the report.",
            file_source="/local/path/to/report.pdf"
        ))
        """
        if urlparse(req.file_source).scheme in ("http", "https"):
            return await self._send_file_by_url_async(req)
            
        return await self._send_file_by_upload_async(req)

    async def _send_file_by_url_async(self, req: SendFileReq) -> Optional[Message]:
        ext = self._get_extension(req.file_source)
        upload_type = self._determine_upload_type(ext)

        if upload_type == UploadType.IMAGE:
            attachment = Attachment(type=AttachmentType.IMAGE, payload={"url": req.file_source})
            return await self._send_file_internal_async(req, attachment)

        temp_path = None
        try:
            temp_path = await self._download_temp_file_async(req.file_source)
            req_copy = req.model_copy(update={"file_source": temp_path})
            return await self._send_file_by_upload_async(req_copy)
        except Exception as e:
            logger.error(f"Async file processing/upload error: {e}")
            raise
        finally:
            if temp_path and os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except OSError as e:
                    logger.error(f"Failed to cleanup temp file: {e}")

    async def _send_file_by_upload_async(self, req: SendFileReq) -> Optional[Message]:
        ext = self._get_extension(req.file_source)
        u_type = self._determine_upload_type(ext)

        upload_req = UploadFileReq(type=u_type, file_path=req.file_source)
        upload_resp = await self.uploads.upload_file_async(upload_req)

        if not upload_resp or not upload_resp.token:
            return None

        attachment = self._build_attachment_from_token(u_type, upload_resp.token, Path(req.file_source).name)
        return await self._send_file_internal_async(req, attachment)

    async def _send_file_internal_async(self, req: SendFileReq, attachment: Attachment) -> Message:
        attachments: List[Attachment] = req.attachments or []
        attachments.append(attachment)

        request_data = SendMessageReq(
            user_id=req.user_id,
            chat_id=req.chat_id,
            text=req.text,
            format=req.format,
            attachments=attachments,
            notify=req.notify,
            link=req.link,
            disable_link_preview=req.disable_link_preview
        )

        query, payload = self.client.split_request(request_data)
        last_err: Optional[Exception] = None
        
        for _ in range(self.client.max_retries):
            try:
                return await self.client.adecode("POST", Paths.MESSAGES, Message, query=query, payload=payload)
            except Exception as e:
                last_err = e
                if "not.ready" in str(e).lower():
                    await asyncio.sleep(self.client.retry_delay_sec)
                    continue
                break

        if last_err:
            raise last_err
        raise Exception("Unknown error in sendFileInternalAsync")

    def _get_extension(self, source: str) -> str:
        parsed = urlparse(source)
        path = parsed.path if parsed.scheme and parsed.netloc else source
        return Path(path).suffix.lower()

    def _determine_upload_type(self, ext: str) -> UploadType:
        if ext in {".jpg", ".jpeg", ".png", ".webp"}:
            return UploadType.IMAGE
        if ext in {".mp4", ".avi", ".mov"}:
            return UploadType.VIDEO
        if ext in {".mp3", ".ogg", ".wav"}:
            return UploadType.AUDIO
        return UploadType.FILE
    
    def _sanitize_filename(self, filename: str) -> str:
        base = os.path.basename(filename)
        return re.sub(r'[^a-zA-Z0-9.\-_]', '_', base)

    def _build_attachment_from_token(self, u_type: UploadType, token: str, filename: str) -> Attachment:
        payload: dict[str, Any] = {"token": token}
        if u_type == UploadType.FILE:
            payload["filename"] = filename
        return Attachment(type=AttachmentType(u_type.value), payload=payload)

    def _download_temp_file(self, url_str: str) -> str:
        headers = {"User-Agent": "maxbot-client/1.0"}
        with httpx.Client(follow_redirects=True, max_redirects=3) as client:
            with client.stream("GET", url_str, headers=headers) as resp:
                resp.raise_for_status() 

                content_disp = resp.headers.get("Content-Disposition", "")
                filename = None
                if "filename=" in content_disp:
                    raw_part = content_disp.split("filename=")[1].split(";")[0]
                    raw_filename = raw_part.strip('"').strip("'")
                    filename = self._sanitize_filename(raw_filename)
                
                if not filename:
                    content_type = resp.headers.get("Content-Type", "")
                    ext = mimetypes.guess_extension(content_type.split(";")[0])
                    if ext:
                        filename = f"file{ext}"

                if not filename:
                    filename = os.path.basename(Path(urlparse(url_str).path).name) or "temp_file.bin"

                fd, temp_path = tempfile.mkstemp(prefix="temp_", suffix=f"_{os.path.basename(filename)}")
                try:
                    with os.fdopen(fd, "wb") as f:
                        for chunk in resp.iter_bytes(chunk_size=8192):
                            f.write(chunk)
                    return temp_path
                except Exception:
                    os.remove(temp_path)
                    raise
    
    async def _download_temp_file_async(self, url_str: str) -> str:
        headers = {"User-Agent": "maxbot-client/1.0"}
        async with httpx.AsyncClient() as client:
            async with client.stream("GET", url_str, headers=headers, follow_redirects=True) as resp:
                resp.raise_for_status()

                content_type = resp.headers.get("Content-Type", "").split(";")[0]
                extension = mimetypes.guess_extension(content_type) or ".bin"

                url_path_name = os.path.basename(Path(urlparse(url_str).path).name)
                if url_path_name == "uc" or not url_path_name:
                    filename = f"file{extension}"
                else:
                    filename = url_path_name if "." in url_path_name else f"{url_path_name}{extension}"

                fd, temp_path = tempfile.mkstemp(prefix="temp_", suffix=f"_{os.path.basename(filename)}")
                os.close(fd)

                async with aiofiles.open(temp_path, "wb") as f:
                    async for chunk in resp.aiter_bytes(chunk_size=8192):
                        await f.write(chunk)
                return temp_path