from typing import Any

from maxbot_api_client_python.client import Client
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types.models import BotInfo, BotPatch

class Bots:
    def __init__(self, client: Client):
        self.client = client

    def get_bot(self) -> BotInfo:
        """
        Retrieves information about the current bot, such as its user ID, name, and description.

        Example:
            response = bot.bots.get_bot()
        """
        return self.client.decode("GET", Paths.ME, BotInfo)

    def patch_bot(self, req: BotPatch) -> BotInfo:
        """
        Edits current bot info.
        Fill only the fields you want to update - all remaining fields will stay untouched.

        Example:
            response = bot.bots.patch_bot(BotPatch(
                name="New Name",
                description="New description"
            ))
        """
        query, payload = self.client.split_request(req)
        return self.client.decode("PATCH", Paths.ME, BotInfo, query=query, payload=payload)
    
    async def get_bot_async(self) -> BotInfo:
        """
        Async version of get_bot.
        
        Example:
            response = await bot.bots.get_bot_async()
        """
        return await self.client.adecode("GET", Paths.ME, BotInfo)
    
    async def patch_bot_async(self, req: BotPatch) -> BotInfo:
        """
        Async version of patch_bot.

        Example:
            response = await bot.bots.patch_bot_async(BotPatch(
                name="New Name",
                description="New description"
            ))
        """
        query, payload = self.client.split_request(req)
        return await self.client.adecode("PATCH", Paths.ME, BotInfo, query=query, payload=payload)