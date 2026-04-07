from maxbot_api_client_python.api import API, Config

def main():
    try:
        with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN",
            ratelimiter=25,
            timeout=30
        )) as bot:
            
            bot.messages.SendMessage(
                user_id=1234567890,
                text="Hello world!"
            )
            print("SendMessage success!")
            
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()