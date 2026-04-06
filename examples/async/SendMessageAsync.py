import asyncio
from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types import models


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
        
    target_user_id = 123456789 # recipient user ID

    try:
        await bot.messages.SendMessageAsync(models.SendMessageReq(
            user_id=target_user_id,
            text="Hello world!"
        ))
        print("SendMessageAsync success!")
    except Exception as e:
        print(f"SendMessageAsync error: {e}")
    finally:
        await bot.aclose()

if __name__ == "__main__":
    asyncio.run(main())
