import asyncio
from maxbot_api_client_python.api import API, Config

async def main():
    target_user_id = 123456789 # recipient user ID

    try:
        async with API(Config(
            base_url="https://platform-api.max.ru",
            token="YOUR_BOT_TOKEN"
        )) as bot:

            await bot.messages.SendMessageAsync(
                user_id=target_user_id,
                text="Hello world!"
            )
            print("SendMessageAsync success!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())