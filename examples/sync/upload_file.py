from maxbot_api_client_python import API, Config
from maxbot_api_client_python.types.constants import UploadType
from maxbot_api_client_python.types.models import UploadFileReq, SendMessageReq
from maxbot_api_client_python.utils import attach_image

def main():
    try:
        with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN",
            ratelimiter=25,
            timeout=30
        )) as bot:

            upload_request = UploadFileReq(
                type=UploadType.IMAGE,
                file_path="examples/assets/file.jpg"
            )
            file_info = bot.uploads.upload_file(upload_request)
            
            if file_info and file_info.token:
                message_request = SendMessageReq(
                    user_id=123456789,    # recipient user ID
                    attachments=[attach_image(token=file_info.token)]
                )
                bot.messages.send_message(message_request)
                print("File successfully sent to chat!")

    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()