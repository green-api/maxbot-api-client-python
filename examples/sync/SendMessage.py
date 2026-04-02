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
            global_rps=25,
            timeout=35
        ))
    except ValueError as e:
        log.error(f"Initialization error: {e}")
        return
    try:
        bot.messages.SendMessage(SendMessageReq(
        user_id=1234567890,
        text="Hello world!"
    ))
        log.info("SendMessage success!")
    except Exception as e:
        log.error(f"SendMessage error: {e}")
    finally:
        bot.close()
        
if __name__ == "__main__":
    main()