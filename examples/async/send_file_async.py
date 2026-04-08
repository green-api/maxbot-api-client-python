import asyncio
from maxbot_api_client_python import API, Config
from maxbot_api_client_python.types.models import SendFileReq

async def main():
    try:
        async with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN"
        )) as bot:

            req = SendFileReq(
                user_id=123456789,    # recipient user ID
                text="Check this!",
                file_source="https://storage.yandexcloud.net/sw-prod-03-test/ChatBot/corgi.jpg"
            )
            response = await bot.helpers.send_file_async(req)
            
            if response:
                print("send_file_async success!")
            else:
                print("send_file_async failed to process the file.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())