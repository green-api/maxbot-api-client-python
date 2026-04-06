from maxbot_api_client_python.client import Client, decode, adecode
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types import models

class Subscriptions:
    def __init__(self, client: Client):
        self.client = client

    def GetSubscriptions(self) -> models.GetSubscriptionsResp:
        """
        Returns a list of all subscriptions if your bot receives data via a Webhook.

        Example:
            response = api.subscriptions.GetSubscriptions()
        """
        return decode(self.client, "GET", Paths.SUBSCRIPTIONS,  models.GetSubscriptionsResp)

    def Subscribe(self, req: models.SubscribeReq) -> models.SimpleQueryResult:
        """
        Configures the delivery of bot events via Webhook.

        Example:
            response = api.subscriptions.Subscribe(SubscribeReq(
                url="https://webhook.site/endpoint"
            ))
        """
        return decode(self.client, "POST", Paths.SUBSCRIPTIONS,  models.SimpleQueryResult, payload=req)

    def Unsubscribe(self, req: models.UnsubscribeReq) -> models.SimpleQueryResult:
        """
        Unsubscribes the bot from receiving updates via Webhook.

        Example:
            response = api.subscriptions.Unsubscribe(UnsubscribeReq(
                url="https://webhook.site/endpoint"
            ))
        """
        return decode(self.client, "DELETE", Paths.SUBSCRIPTIONS,  models.SimpleQueryResult, query=req.model_dump(exclude_none=True))

    def GetUpdates(self, req: models.GetUpdatesReq) -> models.GetUpdatesResp:
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
        return decode(self.client, "GET", Paths.UPDATES, models.GetUpdatesResp, query=req.model_dump(exclude_none=True))

    async def GetSubscriptionsAsync(self) -> models.GetSubscriptionsResp:
        """
        Async version of GetSubscriptions.

        Example:
            response = await api.subscriptions.GetSubscriptionsAsync()
        """
        return await adecode(self.client, "GET", Paths.SUBSCRIPTIONS,  models.GetSubscriptionsResp)

    async def SubscribeAsync(self, req: models.SubscribeReq) -> models.SimpleQueryResult:
        """
        Async version of Subscribe.

        Example:
            response = await api.subscriptions.SubscribeAsync(SubscribeReq(
                url="https://webhook.site/endpoint"
            ))
        """
        return await adecode(self.client, "POST", Paths.SUBSCRIPTIONS,  models.SimpleQueryResult, payload=req)
    
    async def UnsubscribeAsync(self, req: models.UnsubscribeReq) -> models.SimpleQueryResult:
        """
        Async version of Unsubscribe.

        Example:
            response = await api.subscriptions.UnsubscribeAsync(UnsubscribeReq(
                url="https://webhook.site/endpoint"
            ))
        """
        return await adecode(self.client, "DELETE", Paths.SUBSCRIPTIONS,  models.SimpleQueryResult, query=req.model_dump(exclude_none=True))
    
    async def GetUpdatesAsync(self, req: models.GetUpdatesReq) -> models.GetUpdatesResp:
        """
        Async version of GetUpdates.

        Example:
            response = await api.subscriptions.GetUpdatesAsync(GetUpdatesReq(
                marker=123456789,
                timeout=30  # seconds to wait for new updates
            ))
        """
        return await adecode(self.client, "GET", Paths.UPDATES, models.GetUpdatesResp, query=req.model_dump(exclude_none=True))
    