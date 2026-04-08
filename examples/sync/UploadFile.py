from maxbot_api_client_python import API, Config
from maxbot_api_client_python.types.constants import UploadType
from maxbot_api_client_python.utils import attach_image

def main():
    try:
        with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN",
            ratelimiter=25,
            timeout=30
        )) as bot:

            file_info = bot.uploads.upload_file(
                type=UploadType.IMAGE,
                file_path="examples/assets/file.jpg"
            )
            
            if file_info and file_info.token:
                bot.messages.send_message(
                    user_id=123456789,    # recipient user ID
                    attachments=[attach_image(token=file_info.token)]
                )
                print("File successfully sent to chat!")

    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()