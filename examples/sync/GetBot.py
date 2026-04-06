from maxbot_api_client_python.api import API, Config

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
        response = bot.bots.GetBot()
        print(f"Bot info received: {response.model_dump()}")
    except Exception as e:
        print(f"GetBot error: {e}")
    finally:
        bot.close()

if __name__ == "__main__":
    main()