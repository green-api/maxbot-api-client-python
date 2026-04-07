import asyncio
from maxbot_api_client_python.api import API, Config

async def main():
    target_user_id = 123456789

    try:
        async with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN"
        )) as bot:

            response = await bot.helpers.SendFileAsync(
                user_id=target_user_id,
                text="Check this!",
                file_source="https://storage.yandexcloud.net/sw-prod-03-test/ChatBot/corgi.jpg"
            )
            
            if response:
                print("SendFileAsync success!")
            else:
                print("SendFileAsync failed to process the file.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())