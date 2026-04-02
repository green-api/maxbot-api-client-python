import asyncio, logging
from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.models import *

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

async def main():
    try:
        bot = API(Config(
            base_url="https://platform-api.max.ru",  # Base url for MAX API requests
            token="YOUR_BOT_TOKEN",                  # Max bot token
            global_rps=25,
            timeout=35
        ))
    except ValueError as e:
        log.error(f"Initialization error: {e}")
        return
        
    target_user_id = 123456789 # recipient user ID

    try:
        await bot.messages.SendMessageAsync(SendMessageReq(
            user_id=target_user_id,
            text="Hello world!"
        ))
        log.info("SendMessageAsync success!")
    except Exception as e:
        log.error(f"SendMessageAsync error: {e}")
    finally:
        await bot.aclose()

if __name__ == "__main__":
    asyncio.run(main())