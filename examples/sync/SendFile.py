import logging
from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.models import SendFileReq

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
        response = bot.helpers.SendFile(SendFileReq(
            chat_id=1234567890,
            text="Check this!",
            file_source="https://http.cat/200.jpg"
        ))
        log.info(f"SendFile success! Message ID: {response.message_id}") if response else log.error("SendFile failed to process the file.")
            
    except Exception as e:
        log.error(f"SendFile error: {e}")
    finally:
        bot.close()

if __name__ == "__main__":
    main()