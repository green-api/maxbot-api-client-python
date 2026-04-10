import asyncio, logging

from pathlib import Path
from typing import Any, Optional
from tenacity import AsyncRetrying, retry, stop_after_attempt, wait_exponential

from maxbot_api_client_python.client import Client
from maxbot_api_client_python.types.constants import Paths, UploadType
from maxbot_api_client_python.types.models import UploadedInfo, UploadFileReq, PhotoAttachmentRequestPayload

logger = logging.getLogger(__name__)

class Uploads:
    def __init__(self, client: Client):
        self.client = client

    @retry(
        stop=stop_after_attempt(3), 
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True,
    )
    def upload_file(self, req: UploadFileReq) -> UploadedInfo:
        """
        Uploads a file to the server and returns the upload metadata.
        It seamlessly handles both STEP 1 (obtaining the URL) and STEP 2 (streaming the file).

        Example:
            response = bot.uploads.upload_file(UploadFileReq(
                type=UploadType.IMAGE,
                file_path="/path/to/image.png"
            ))
        """
        init_resp = self.get_upload_url(req.type)
        
        if init_resp.url:
            if not req.file_path:
                raise ValueError("file_path must be provided for multipart uploads.")
                
            multipart_resp = self.upload_multipart(init_resp.url, req.file_path)

            if multipart_resp:
                if multipart_resp.token:
                    return multipart_resp

                if multipart_resp.photos:
                    first_photo = next(iter(multipart_resp.photos.values()), None)
                    if first_photo and first_photo.token:
                        multipart_resp.token = first_photo.token
                        return multipart_resp

        if init_resp.token:
            return UploadedInfo(token=init_resp.token)

        raise Exception("Server did not return token after upload")

    def get_upload_url(self, upload_type: UploadType) -> PhotoAttachmentRequestPayload:
        """Internal helper: Obtains the target URL for uploading."""
        return self.client.decode("POST", Paths.UPLOADS, PhotoAttachmentRequestPayload, query={"type": upload_type.value})

    def upload_multipart(self, upload_url: str, file_path: str) -> Optional[UploadedInfo]:
        """Internal helper: Streams the file to the obtained URL."""
        path = Path(file_path)
        try:
            with open(path, "rb") as f:
                safe_name = path.name[:255]
                files = {"file": (safe_name, f)}
                return self.client.decode("POST", upload_url, UploadedInfo, files=files)
        except OSError as e:
            logger.error(f"Failed to read file for upload: {e}")
            return None

    async def upload_file_async(self, req: UploadFileReq) -> UploadedInfo:
        """
        Async version of upload_file.

        Example:
            response = await bot.uploads.upload_file_async(UploadFileReq(
                type=UploadType.IMAGE,
                file_path="/path/to/image.png"
            ))
        """
        async for attempt in AsyncRetrying(
            stop=stop_after_attempt(3), 
            wait=wait_exponential(multiplier=1, min=2, max=10),
            reraise=True
        ):
            with attempt:
                init_resp = await self.get_upload_url_async(req.type) 
                if init_resp.url:
                    if not req.file_path:
                        raise ValueError("file_path must be provided for multipart uploads.")
                    
                    multipart_resp = await self.upload_multipart_async(init_resp.url, req.file_path)
                    
                    if multipart_resp:
                        if multipart_resp.token:
                            return multipart_resp

                        if multipart_resp.photos:
                            first_photo = next(iter(multipart_resp.photos.values()), None)
                            if first_photo and first_photo.token:
                                multipart_resp.token = first_photo.token
                                return multipart_resp

                if init_resp.token:
                    return UploadedInfo(token=init_resp.token)
                
                raise Exception("Server did not return token after upload")

    async def get_upload_url_async(self, upload_type: UploadType) -> PhotoAttachmentRequestPayload:
        return await self.client.adecode("POST", Paths.UPLOADS, PhotoAttachmentRequestPayload, query={"type": upload_type.value})

    async def upload_multipart_async(self, upload_url: str, file_path: str) -> Optional[UploadedInfo]:
        path = Path(file_path)
        try:
            with open(path, "rb") as f:
                safe_name = path.name[:255]
                files = {"file": (safe_name, f)}
                return await self.client.adecode("POST", upload_url, UploadedInfo, files=files)
        except OSError as e:
            logger.error(f"Failed to read file for upload: {e}")
            return None