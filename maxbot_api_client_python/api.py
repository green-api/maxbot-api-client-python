from typing import Any, Self

from maxbot_api_client_python.client import Client
from maxbot_api_client_python.types.models import Config
from maxbot_api_client_python import tools

class API:
    def __init__(self, cfg: Config) -> None:
        self.client = Client(cfg)

        self.bots = tools.Bots(self.client)
        self.chats = tools.Chats(self.client)
        self.helpers = tools.Helpers(self.client)
        self.messages = tools.Messages(self.client)
        self.subscriptions = tools.Subscriptions(self.client)
        self.uploads = tools.Uploads(self.client)

    def __enter__(self) -> Self:
        self.client.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.client.__exit__(exc_type, exc_val, exc_tb)

    async def __aenter__(self) -> Self:
        await self.client.__aenter__()
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        await self.client.__aexit__(exc_type, exc_val, exc_tb)

    def close(self) -> None:
        self.client.close()

    async def aclose(self) -> None:
        await self.client.aclose()