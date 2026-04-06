import asyncio
from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.models import GetUpdatesReq


async def main():
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
        response = await bot.subscriptions.GetUpdatesAsync(GetUpdatesReq())
        print(f"New update received: {response.model_dump()}")
    except Exception as e:
        print(f"GetUpdatesAsync error: {e}")
    finally:
        await bot.aclose()

if __name__ == "__main__":
    asyncio.run(main())