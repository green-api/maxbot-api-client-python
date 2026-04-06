from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.models import UploadFileReq, SendMessageReq
from maxbot_api_client_python.utils import attach_image

def main():
    try:
        bot = API(Config(
            base_url="https://platform-api.max.ru",  # Base url for MAX API requests
            token="YOUR_BOT_TOKEN",                  # Max bot token
            ratelimiter=25,
            timeout=30
        ))
    except ValueError as e:
        print(f"Initialization error: {e}")
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
            print("File successfully sent to chat!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        bot.close()
        
if __name__ == "__main__":
    main()