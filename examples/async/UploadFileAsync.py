import asyncio, logging
from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.models import *
from maxbot_api_client_python.utils import attach_image

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

async def main():
    try:
        bot = API(Config(
            base_url="https://platform-api.max.ru",  # Base url for MAX API requests
            token="YOUR_BOT_TOKEN",                  # Max bot token
            ratelimiter=25,
            timeout=30
        ))
    except ValueError as e:
        log.error(f"Initialization error: {e}")
        return
    
    target_user_id = 123456789 # recipient user ID

    try:
        response = await bot.uploads.UploadFileAsync(UploadFileReq(
            type=U"image",
            file_path="examples/assets/file.jpg"
        ))
        
        if response and response.token:
            await bot.messages.SendMessageAsync(SendMessageReq(
                user_id=target_user_id,
                attachments=[attach_image(token=response.token)]
            ))
            log.info("File successfully sent to chat!")

    except Exception as e:
        log.error(f"Error: {e}")
    finally:
        await bot.aclose()

if __name__ == "__main__":
    asyncio.run(main())