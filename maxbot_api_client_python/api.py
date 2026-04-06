from maxbot_api_client_python.client import Client, Config
from maxbot_api_client_python import tools

class API:
    def __init__(self, cfg: Config):
        self.client = Client(cfg)

        self.bots = tools.Bots(self.client)
        self.chats = tools.Chats(self.client)
        self.helpers = tools.Helpers(self.client)
        self.messages = tools.Messages(self.client)
        self.subscriptions = tools.Subscriptions(self.client)
        self.uploads = tools.Uploads(self.client)

    def close(self):
        self.client.close()

    async def aclose(self):
        await self.client.aclose()
