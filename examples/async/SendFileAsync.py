import asyncio
from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.models import SendFileReq


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
        response = await bot.helpers.SendFileAsync(SendFileReq(
            user_id=target_user_id,
            text="Check this!",
            file_source="https://http.cat/200.jpg"
        ))
        print(f"SendFileAsync success!") if response else print("SendFileAsync failed to process the file.")

    except Exception as e:
        print(f"SendFileAsync error: {e}")
    finally:
        await bot.aclose()

if __name__ == "__main__":
    asyncio.run(main())