from maxbot_api_client_python import API, Config
from maxbot_api_client_python.types.models import SendMessageReq

def main():
    try:
        with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN",
            ratelimiter=25,
            timeout=30
        )) as bot:
            
            req = SendMessageReq(
                user_id=123456789,    # recipient user ID
                text="Hello world!"
            )
            bot.messages.send_message(req)
            print("send_message success!")
            
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()