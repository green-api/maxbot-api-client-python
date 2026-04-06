from maxbot_api_client_python.api import API, Config
from maxbot_api_client_python.types.models import SendFileReq

def main():
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
        response = bot.helpers.SendFile(SendFileReq(
            user_id=1234567890,
            text="Check this!",
            file_source="https://http.cat/200.jpg"
        ))
        print(f"SendFile success! Message ID: {response.message_id}") if response else print("SendFile failed to process the file.")
            
    except Exception as e:
        print(f"SendFile error: {e}")
    finally:
        bot.close()

if __name__ == "__main__":
    main()