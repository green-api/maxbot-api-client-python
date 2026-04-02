from maxbot_api_client_python.client import Client, decode, adecode
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types.models import *

class Subscriptions:
    def __init__(self, client: Client):
        self.client = client

    def GetSubscriptions(self) -> GetSubscriptionsResp:
        """
        Returns a list of all subscriptions if your bot receives data via a Webhook.

        Example:
            response = api.subscriptions.GetSubscriptions()
        """
        return decode(self.client, "GET", Paths.SUBSCRIPTIONS, GetSubscriptionsResp)

    def Subscribe(self, req: SubscribeReq) -> SimpleQueryResult:
        """
        Configures the delivery of bot events via Webhook.

        Example:
            response = api.subscriptions.Subscribe(SubscribeReq(
                url="https://webhook.site/endpoint"
            ))
        """
        return decode(self.client, "POST", Paths.SUBSCRIPTIONS, SimpleQueryResult, payload=req)

    def Unsubscribe(self, req: UnsubscribeReq) -> SimpleQueryResult:
        """
        Unsubscribes the bot from receiving updates via Webhook.

        Example:
            response = api.subscriptions.Unsubscribe(UnsubscribeReq(
                url="https://webhook.site/endpoint"
            ))
        """
        return decode(self.client, "DELETE", Paths.SUBSCRIPTIONS, SimpleQueryResult, query=req.model_dump(exclude_none=True))

    def GetUpdates(self, req: GetUpdatesReq) -> GetUpdatesResp:
        """
        Fetches new events (incoming messages, bot additions, etc.) from the server.
        Use this method for long-polling. Provide a Marker to acknowledge previous 
        updates and fetch only new ones.

        Example:
            response = api.subscriptions.GetUpdates(GetUpdatesReq(
                marker=123456789,
                timeout=30  # seconds to wait for new updates
            ))
        """
        return decode(self.client, "GET", Paths.UPDATES, GetUpdatesResp, query=req.model_dump(exclude_none=True))

    async def GetSubscriptionsAsync(self) -> GetSubscriptionsResp:
        """
        Async version of GetSubscriptions.

        Example:
            response = await api.subscriptions.GetSubscriptionsAsync()
        """
        return await adecode(self.client, "GET", Paths.SUBSCRIPTIONS, GetSubscriptionsResp)

    async def SubscribeAsync(self, req: SubscribeReq) -> SimpleQueryResult:
        """
        Async version of Subscribe.

        Example:
            response = await api.subscriptions.SubscribeAsync(SubscribeReq(
                url="https://webhook.site/endpoint"
            ))
        """
        return await adecode(self.client, "POST", Paths.SUBSCRIPTIONS, SimpleQueryResult, payload=req)
    
    async def UnSubscribeAsync(self, req: UnsubscribeReq) -> SimpleQueryResult:
        """
        Async version of Unsubscribe.

        Example:
            response = await api.subscriptions.UnSubscribeAsync(UnsubscribeReq(
                url="https://webhook.site/endpoint"
            ))
        """
        return await adecode(self.client, "DELETE", Paths.SUBSCRIPTIONS, SimpleQueryResult, query=req.model_dump(exclude_none=True))
    
    async def GetUpdatesAsync(self, req: GetUpdatesReq) -> GetUpdatesResp:
        """
        Async version of GetUpdates.

        Example:
            response = await api.subscriptions.GetUpdatesAsync(GetUpdatesReq(
                marker=123456789,
                timeout=30  # seconds to wait for new updates
            ))
        """
        return await adecode(self.client, "GET", Paths.UPDATES, GetUpdatesResp, query=req.model_dump(exclude_none=True))
    