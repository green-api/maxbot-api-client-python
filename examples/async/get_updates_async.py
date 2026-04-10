import asyncio
from maxbot_api_client_python import API, Config
from maxbot_api_client_python.types.models import GetUpdatesReq

async def main():
    try:
        async with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN"
        )) as bot:

            request = GetUpdatesReq()
            response = await bot.subscriptions.get_updates_async(request)
            print(f"New update received:\n{response.model_dump_json(indent=4)}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())