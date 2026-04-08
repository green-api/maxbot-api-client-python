import asyncio
from maxbot_api_client_python import API, Config
from maxbot_api_client_python.types.models import SendMessageReq

async def main():
    try:
        async with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN"
        )) as bot:

            req = SendMessageReq(
                user_id=123456789,    # recipient user ID
                text="Hello world!"
            )
            await bot.messages.send_message_async(req)
            print("send_message_async success!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())