import logging
from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.models import *
from maxbot_api_client_python.utils import attach_image

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
    
    target_user_id=123456789  # recipient user ID

    try:
        file_info = bot.uploads.UploadFile(UploadFileReq(
            type="image",
            file_path="examples/assets/file.jpg"
        ))
        if file_info and file_info.token:
            bot.messages.SendMessage(SendMessageReq(
                user_id=target_user_id,
                attachments=[attach_image(token=file_info.token)]
            ))
            log.info("File successfully sent to chat!")

    except Exception as e:
        log.error(f"Error: {e}")
    finally:
        bot.close()
        
if __name__ == "__main__":
    main()