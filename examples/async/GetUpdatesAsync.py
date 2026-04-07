import asyncio
from maxbot_api_client_python.api import API, Config

async def main():
    try:
        async with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN"
        )) as bot:

            response = await bot.subscriptions.GetUpdatesAsync()
            print(f"New update received:\n{response.model_dump_json(indent=4)}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())