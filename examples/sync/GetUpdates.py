import logging
from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.models import *

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

def main():
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

    try:
        response = bot.subscriptions.GetUpdates(GetUpdatesReq())
        log.info(f"New update received: {response.model_dump()}")
    except Exception as e:
        log.error(f"GetUpdates error: {e}")
    finally:
        bot.close()

if __name__ == "__main__":
    main()