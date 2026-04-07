from maxbot_api_client_python.api import API, Config

def main():
    try:
        with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN",
            ratelimiter=25,
            timeout=30
        )) as bot:

            response = bot.helpers.SendFile(
                user_id=1234567890,
                text="Check this!",
                file_source="https://http.cat/200.jpg"
            )
            
            if response:
                print("SendFile success!")
            else:
                print("SendFile failed to process the file.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()