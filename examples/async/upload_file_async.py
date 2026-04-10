import asyncio
from maxbot_api_client_python import API, Config
from maxbot_api_client_python.types.constants import UploadType
from maxbot_api_client_python.types.models import UploadFileReq, SendMessageReq
from maxbot_api_client_python.utils import attach_image

async def main():
    try:
        async with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN"
        )) as bot:

            upload_request = UploadFileReq(
                type=UploadType.IMAGE,
                file_path="examples/assets/file.jpg"
            )
            response = await bot.uploads.upload_file_async(upload_request)
            
            if response and response.token:
                message_request = SendMessageReq(
                    user_id=123456789,    # recipient user ID
                    attachments=[attach_image(token=response.token)]
                )
                await bot.messages.send_message_async(message_request)
                print("File successfully sent to chat!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())