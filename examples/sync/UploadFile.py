from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.constants import UploadType
from maxbot_api_client_python.utils import attach_image

def main():
    target_user_id = 123456789  # recipient user ID

    try:
        with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN",
            ratelimiter=25,
            timeout=30
        )) as bot:

            file_info = bot.uploads.UploadFile(
                type=UploadType.image,
                file_path="examples/assets/file.jpg"
            )
            
            if file_info and file_info.token:
                bot.messages.SendMessage(
                    user_id=target_user_id,
                    attachments=[attach_image(token=file_info.token)]
                )
                print("File successfully sent to chat!")

    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()