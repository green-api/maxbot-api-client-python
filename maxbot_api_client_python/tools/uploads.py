import asyncio

from pathlib import Path
from typing import Optional
from tenacity import retry, stop_after_attempt, wait_exponential

from maxbot_api_client_python.client import Client, decode
from maxbot_api_client_python.types.constants import Paths, UploadType
from maxbot_api_client_python.types.models import *

class Uploads:
    def __init__(self, client: Client):
        self.client = client

    @retry(
        stop=stop_after_attempt(3), 
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True,
    )

    def UploadFile(self, req: UploadFileReq) -> UploadedInfo:
        """
        Uploads a file to the server and returns the upload metadata.
        It seamlessly handles both STEP 1 (obtaining the URL) and STEP 2 (streaming the file).

        Example:
            response = api.uploads.UploadFile(UploadFileReq(
                type=UploadType.IMAGE,
                file_path="/path/to/image.png"
            ))
        """
        init_resp = self.get_upload_url(req.type)
        
        if init_resp.url:
            multipart_resp = self.upload_multipart(init_resp.url, req.file_path)

            if multipart_resp and multipart_resp.token:
                return multipart_resp

            if multipart_resp and multipart_resp.photos:
                first_photo = next(iter(multipart_resp.photos.values()), None)
                if first_photo and first_photo.token:
                    multipart_resp.token = first_photo.token
                    return multipart_resp

        if init_resp.token:
            return UploadedInfo(token=init_resp.token)

        raise Exception("Server did not return token after upload")

    def get_upload_url(self, upload_type: UploadType) -> PhotoAttachmentRequestPayload:
        """Internal helper: Obtains the target URL for uploading."""
        return decode(self.client, "POST", Paths.UPLOADS, PhotoAttachmentRequestPayload, query={"type": upload_type.value})

    def upload_multipart(self, upload_url: str, file_path: str) -> Optional[UploadedInfo]:
        """Internal helper: Streams the file to the obtained URL."""
        path = Path(file_path)
        try:
            with open(path, "rb") as f:
                files = {"file": (path.name, f)}
                return decode(self.client, "POST", upload_url, UploadedInfo, files=files)
        except OSError as e:
            Client.logger.error(f"Failed to read file for upload: {e}")
            return None

    async def UploadFileAsync(self, req: UploadFileReq) -> UploadedInfo:
        """
        Async version of UploadFile.

        Example:
            response = await api.uploads.UploadFileAsync(UploadFileReq(
                type=UploadType.IMAGE,
                file_path="/path/to/image.png"
            ))
        """
        return await asyncio.to_thread(self.UploadFile, req)

    async def get_upload_url_async(self, upload_type: UploadType) -> PhotoAttachmentRequestPayload:
        """Async version of get_upload_url."""
        return await asyncio.to_thread(self.get_upload_url, upload_type)

    async def upload_multipart_async(self, upload_url: str, file_path: str) -> Optional[UploadedInfo]:
        """Async version of upload_multipart."""
        return await asyncio.to_thread(self.upload_multipart, upload_url, file_path)