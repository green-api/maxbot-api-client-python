from maxbot_api_client_python.client import Client, decode, adecode
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types.models import *

class Bots:
    def __init__(self, client: Client):
        self.client = client

    def GetBot(self) -> BotInfo:
        """
        Retrieves information about the current bot, such as its user ID, name, and description.

        Example:
            response = api.bots.GetBot()
        """
        return decode(self.client, "GET", Paths.ME, BotInfo)

    def PatchBot(self, req: BotPatch) -> BotInfo:
        """
        Edits current bot info.
        Fill only the fields you want to update - all remaining fields will stay untouched.

        Example:
            response = api.bots.PatchBot(BotPatch(
                name="New Name",
                description="New description"
            ))
        """
        return decode(self.client, "PATCH", Paths.ME, BotInfo, payload=req)
    
    async def GetBotAsync(self) -> BotInfo:
        """
        Async version of GetBot.
        
        Example:
            response = await api.bots.GetBotAsync()
        """
        return await adecode(self.client, "GET", Paths.ME, BotInfo)
    
    async def PatchBotAsync(self, req: BotPatch) -> BotInfo:
        """
        Async version of PatchBot.

        Example:
            response = await api.bots.PatchBotAsync(BotPatch(
                name="New Name",
                description="New description"
            ))
        """
        return await adecode(self.client, "PATCH", Paths.ME, BotInfo, payload=req)