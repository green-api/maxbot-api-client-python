import asyncio, os, time, httpx, aiofiles, mimetypes
from typing import Any, List, Optional
from urllib.parse import urlparse
from pathlib import Path

from maxbot_api_client_python.tools.uploads import Uploads
from maxbot_api_client_python.client import Client, decode, adecode
from maxbot_api_client_python.types.constants import AttachmentType, Paths, UploadType
from maxbot_api_client_python.types.models import Message, SendFileReq, SendMessageReq, UploadFileReq, Attachment

class Helpers:
    def __init__(self, client: Client):
        self.client = client
        self.uploads = Uploads(client)

    def SendFile(self, req: SendFileReq) -> Optional[Message]:
        """
        A helper that simplifies sending files to a chat.
        """
        if self._is_url(req.file_source):
            return self.sendFileByUrl(req)
        return self.sendFileByUpload(req)

    def sendFileByUrl(self, req: SendFileReq) -> Optional[Message]:
        ext = self._get_extension(req.file_source)
        upload_type = self._determine_upload_type(ext)

        if upload_type == UploadType.IMAGE:
            attachment = Attachment(type=AttachmentType.IMAGE, payload={"url": req.file_source})
            return self.sendFileInternal(req, attachment)

        temp_path = None
        try:
            temp_path = self._download_temp_file(req.file_source)
            req.file_source = temp_path
            return self.sendFileByUpload(req)
        except Exception as e:
            print(f"File processing/upload error: {e}")
            return None
        finally:
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)

    def sendFileByUpload(self, req: SendFileReq) -> Optional[Message]:
        ext = self._get_extension(req.file_source)
        upload_type = self._determine_upload_type(ext)

        upload_req = UploadFileReq(type=upload_type, file_path=req.file_source)
        upload_resp = self.uploads.UploadFile(upload_req)

        if not upload_resp or not upload_resp.token:
            print("Upload failed: No token returned.")
            return None

        attachment = self._build_attachment_from_token(upload_type, upload_resp.token, Path(req.file_source).name)
        return self.sendFileInternal(req, attachment)

    def sendFileInternal(self, req: SendFileReq, attachment: Attachment) -> Message:
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

        last_err: Optional[Exception] = None
        for _ in range(self.client.max_retries):
            try:
                return decode(self.client, "POST", Paths.MESSAGES, Message, query=request_data.model_dump(exclude_none=True), payload=request_data)
            except Exception as e:
                last_err = e
                if "not.ready" in str(e).lower():
                    time.sleep(self.client.retry_delay_sec)
                    continue
                break

        if last_err:
            raise last_err
        raise Exception("Unknown error in sendFileInternal")

    async def SendFileAsync(self, req: SendFileReq) -> Optional[Message]:
        """
        Async version of SendFile.
        """
        if self._is_url(req.file_source):
            return await self.sendFileByUrlAsync(req)
        return await self.sendFileByUploadAsync(req)

    async def sendFileByUrlAsync(self, req: SendFileReq) -> Optional[Message]:
        ext = self._get_extension(req.file_source)
        upload_type = self._determine_upload_type(ext)

        if upload_type == UploadType.IMAGE:
            attachment = Attachment(type=AttachmentType.IMAGE, payload={"url": req.file_source})
            return await self.sendFileInternalAsync(req, attachment)

        temp_path = None
        try:
            temp_path = await self._download_temp_file_async(req.file_source)
            req.file_source = temp_path
            return await self.sendFileByUploadAsync(req)
        except Exception as e:
            print(f"Async file processing/upload error: {e}")
            return None
        finally:
            if temp_path and os.path.exists(temp_path):
                await asyncio.to_thread(os.remove, temp_path)

    async def sendFileByUploadAsync(self, req: SendFileReq) -> Optional[Message]:
        ext = self._get_extension(req.file_source)
        u_type = self._determine_upload_type(ext)

        upload_req = UploadFileReq(type=u_type, file_path=req.file_source)
        upload_resp = await self.uploads.UploadFileAsync(upload_req) 

        if not upload_resp or not upload_resp.token:
            return None

        attachment = self._build_attachment_from_token(u_type, upload_resp.token, Path(req.file_source).name)
        return await self.sendFileInternalAsync(req, attachment)

    async def sendFileInternalAsync(self, req: SendFileReq, attachment: Attachment) -> Message:
        attachments: List[Attachment] = req.attachments or []
        attachments.append(attachment)

        request_data = SendMessageReq(
            **req.model_dump(exclude={"file_source", "attachments"}),
            attachments=attachments
        )

        last_err: Optional[Exception] = None
        for _ in range(self.client.max_retries):
            try:
                return await adecode(
                    self.client, "POST", Paths.MESSAGES, Message, 
                    query=request_data.model_dump(exclude_none=True), 
                    payload=request_data
                )
            except Exception as e:
                last_err = e
                if "not.ready" in str(e).lower():
                    await asyncio.sleep(self.client.retry_delay_sec)
                    continue
                break

        if last_err:
            raise last_err
        raise Exception("Unknown error in sendFileInternalAsync")
        
    def _is_url(self, source: str) -> bool:
        try:
            result = urlparse(source)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

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

    def _build_attachment_from_token(self, u_type: UploadType, token: str, filename: str) -> Attachment:
        payload: dict[str, Any] = {"token": token}
        if u_type == UploadType.FILE:
            payload["filename"] = filename
        return Attachment(type=AttachmentType(u_type.value), payload=payload)

    def _download_temp_file(self, url_str: str) -> str:
        headers = {"User-Agent": "maxbot-client/1.0"}
        with httpx.Client() as client:
            with client.stream("GET", url_str, headers=headers, follow_redirects=True) as resp:
                resp.raise_for_status() 

                content_disp = resp.headers.get("Content-Disposition", "")
                filename = None
                if "filename=" in content_disp:
                    filename = content_disp.split("filename=")[1].strip('"')
                
                if not filename:
                    content_type = resp.headers.get("Content-Type", "")
                    ext = mimetypes.guess_extension(content_type.split(";")[0])
                    if ext:
                        filename = f"file{ext}"

                if not filename:
                    filename = Path(urlparse(url_str).path).name or "temp_file.bin"

                temp_path = f"temp_{int(time.time())}_{filename}"

                with open(temp_path, "wb") as f:
                    for chunk in resp.iter_bytes(chunk_size=8192):
                        f.write(chunk)
                return temp_path
    
    async def _download_temp_file_async(self, url_str: str) -> str:
        headers = {"User-Agent": "maxbot-client/1.0"}
        async with httpx.AsyncClient() as client:
            async with client.stream("GET", url_str, headers=headers, follow_redirects=True) as resp:
                resp.raise_for_status()

                content_type = resp.headers.get("Content-Type", "").split(";")[0]
                extension = mimetypes.guess_extension(content_type) or ".bin"

                url_path_name = Path(urlparse(url_str).path).name
                if url_path_name == "uc" or not url_path_name:
                    filename = f"file{extension}"
                else:
                    filename = url_path_name if "." in url_path_name else f"{url_path_name}{extension}"

                temp_path = f"temp_{int(time.time())}_{filename}"

                async with aiofiles.open(temp_path, "wb") as f:
                    async for chunk in resp.aiter_bytes(chunk_size=8192):
                        await f.write(chunk)
                return temp_path