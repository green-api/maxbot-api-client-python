from maxbot_api_client_python import API, Config
from maxbot_api_client_python.types.models import GetUpdatesReq

def main():
    try:
        with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN",
            ratelimiter=25,
            timeout=30
        )) as bot:

            request = GetUpdatesReq()
            response = bot.subscriptions.get_updates(request)
            print(f"New update received:\n{response.model_dump_json(indent=4)}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()