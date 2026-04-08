import asyncio
from maxbot_api_client_python import API, Config

async def main():
    try:
        async with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN"
        )) as bot:

            await bot.messages.send_message_async(
                user_id=123456789,    # recipient user ID
                text="Hello world!"
            )
            print("send_message_async success!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())