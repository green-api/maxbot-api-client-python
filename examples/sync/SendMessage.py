from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.models import SendMessageReq

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
    try:
        bot.messages.SendMessage(SendMessageReq(
        user_id=1234567890,
        text="Hello world!"
    ))
        print("SendMessage success!")
    except Exception as e:
        print(f"SendMessage error: {e}")
    finally:
        bot.close()
        
if __name__ == "__main__":
    main()