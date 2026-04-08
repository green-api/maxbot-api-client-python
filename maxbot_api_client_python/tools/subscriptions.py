from typing import Any

from maxbot_api_client_python.client import Client
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types.models import GetSubscriptionsResp, GetUpdatesReq, GetUpdatesResp, SimpleQueryResult, SubscribeReq, UnsubscribeReq

class Subscriptions:
    def __init__(self, client: Client):
        self.client = client

    def get_subscriptions(self) -> GetSubscriptionsResp:
        """
        Returns a list of all subscriptions if your bot receives data via a Webhook.

        Example:
            response = bot.subscriptions.get_subscriptions()
        """
        return self.client.decode("GET", Paths.SUBSCRIPTIONS, GetSubscriptionsResp)

    def subscribe(self, **kwargs: Any) -> SimpleQueryResult:
        """
        Configures the delivery of bot events via Webhook.

        Example:
            response = bot.subscriptions.subscribe(
                url="https://webhook.site/endpoint"
            )
        """
        req = SubscribeReq(**kwargs)
        query, payload = self.client.split_request(req)
        return self.client.decode("POST", Paths.SUBSCRIPTIONS, SimpleQueryResult, query=query, payload=payload)

    def unsubscribe(self, **kwargs: Any) -> SimpleQueryResult:
        """
        Unsubscribes the bot from receiving updates via Webhook.

        Example:
            response = bot.subscriptions.unsubscribe(
                url="https://webhook.site/endpoint"
            )
        """
        req = UnsubscribeReq(**kwargs)
        query, payload = self.client.split_request(req)
        return self.client.decode("DELETE", Paths.SUBSCRIPTIONS, SimpleQueryResult, query=query, payload=payload)

    def get_updates(self, **kwargs: Any) -> GetUpdatesResp:
        """
        Fetches new events (incoming messages, bot additions, etc.) from the server.
        Use this method for long-polling. Provide a Marker to acknowledge previous 
        updates and fetch only new ones.

        Example:
            response = bot.subscriptions.get_updates(
                marker=123456789,
                timeout=30  # seconds to wait for new updates
            )
        """
        req = GetUpdatesReq(**kwargs)
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", Paths.UPDATES, GetUpdatesResp, query=query, payload=payload)

    async def get_subscriptions_async(self) -> GetSubscriptionsResp:
        """
        Async version of get_subscriptions.

        Example:
            response = await bot.subscriptions.get_subscriptions_async()
        """
        return await self.client.adecode("GET", Paths.SUBSCRIPTIONS, GetSubscriptionsResp)

    async def subscribe_async(self, **kwargs: Any) -> SimpleQueryResult:
        """
        Async version of subscribe.

        Example:
            response = await bot.subscriptions.subscribe_async(
                url="https://webhook.site/endpoint"
            )
        """
        req = SubscribeReq(**kwargs)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("POST", Paths.SUBSCRIPTIONS, SimpleQueryResult, query=query, payload=payload)
    
    async def unsubscribe_async(self, **kwargs: Any) -> SimpleQueryResult:
        """
        Async version of unsubscribe.

        Example:
            response = await bot.subscriptions.unsubscribe_async(
                url="https://webhook.site/endpoint"
            )
        """
        req = UnsubscribeReq(**kwargs)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("DELETE", Paths.SUBSCRIPTIONS, SimpleQueryResult, query=query, payload=payload)
    
    async def get_updates_async(self, **kwargs: Any) -> GetUpdatesResp:
        """
        Async version of get_updates.

        Example:
            response = await bot.subscriptions.get_updates_async(
                marker=123456789,
                timeout=30  # seconds to wait for new updates
            )
        """
        req = GetUpdatesReq(**kwargs)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", Paths.UPDATES, GetUpdatesResp, query=query, payload=payload)