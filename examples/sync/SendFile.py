from maxbot_api_client_python import API, Config

def main():
    try:
        with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN",
            ratelimiter=25,
            timeout=30
        )) as bot:

            response = bot.helpers.send_file(
                user_id=123456789,    # recipient user ID
                text="Check this!",
                file_source="https://storage.yandexcloud.net/sw-prod-03-test/ChatBot/corgi.jpg"
            )
            
            if response:
                print("send_file success!")
            else:
                print("send_file failed to process the file.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()