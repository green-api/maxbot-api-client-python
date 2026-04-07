import asyncio
from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.constants import UploadType
from maxbot_api_client_python.utils import attach_image

async def main():
    target_user_id = 123456789 # recipient user ID

    try:
        async with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN"
        )) as bot:

            response = await bot.uploads.UploadFileAsync(
                type=UploadType.image,
                file_path="examples/assets/file.jpg"
            )
            
            if response and response.token:
                await bot.messages.SendMessageAsync(
                    user_id=target_user_id,
                    attachments=[attach_image(token=response.token)]
                )
                print("File successfully sent to chat!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())