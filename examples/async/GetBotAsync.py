import asyncio, logging
from maxbot_api_client_python.api import API, Config

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

    try:
        response = await bot.bots.GetBotAsync()
        log.info(f"Bot info received: {response.model_dump()}")
    except Exception as e:
        log.error(f"GetBotAsync error: {e}")
    finally:
        await bot.aclose()

if __name__ == "__main__":
    asyncio.run(main())