from typing import Any

from maxbot_api_client_python.client import Client
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types.models import AnswerCallbackReq, DeleteMessageReq, EditMessageReq, GetMessageReq, GetMessagesReq, GetVideoInfoReq, GetVideoInfoResp, Message, MessagesList, SendMessageReq, SendMessageResp, SimpleQueryResult

class Messages:
    def __init__(self, client: Client):
        self.client = client

    def get_messages(self, **kwargs: Any) -> MessagesList:
        """
        Retrieves a list of messages.
        It can fetch messages belonging to a specific ChatID or by an exact list of MessageIDs.

        Example:
            # Fetch messages by Chat ID
            response = bot.messages.get_messages(chat_id=123456)
            
            # Fetch specific messages:
            response = bot.messages.get_messages(message_ids=["mid:1", "mid:2"])
        """
        req = GetMessagesReq(**kwargs)
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", Paths.MESSAGES, MessagesList, query=query, payload=payload)

    def send_message(self, **kwargs: Any) -> SendMessageResp:
        """
        Sends a text message or attachment to a specific user or chat.
        If Notify is False, no push notification will be sent to the user.

        Example:
            response = bot.messages.send_message(
                chat_id=123456,
                text="Hello, world!",
                notify=True
            )
        """
        req = SendMessageReq(**kwargs)
        query, payload = self.client.split_request(req)
        return self.client.decode("POST", Paths.MESSAGES, SendMessageResp, query=query, payload=payload)

    def edit_message(self, **kwargs: Any) -> SimpleQueryResult:
        """
        Modifies the content of a previously sent message.

        Example:
            response = bot.messages.edit_message(
                message_id="mid:987654321...",
                text="Updated message text!",
                format="HTML"
            )
        """
        req = EditMessageReq(**kwargs)
        query, payload = self.client.split_request(req)
        return self.client.decode("PUT", Paths.MESSAGES, SimpleQueryResult, query=query, payload=payload)

    def delete_message(self, **kwargs: Any) -> SimpleQueryResult:
        """
        Removes a previously sent message by its ID.

        Example:
            response = bot.messages.delete_message(
                message_id="mid:987654321..."
            )
        """
        req = DeleteMessageReq(**kwargs)
        query, payload = self.client.split_request(req)
        return self.client.decode("DELETE", Paths.MESSAGES, SimpleQueryResult, query=query, payload=payload)

    def get_message(self, **kwargs: Any) -> Message:
        """
        Retrieves full information about a message by its ID.

        Example:
            response = bot.messages.get_message(
                message_id="mid:987654321..."
            )
        """
        req = GetMessageReq(**kwargs)
        path = f"{Paths.MESSAGES}/{req.message_id}"
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", path, Message, query=query, payload=payload)

    def get_video_info(self, **kwargs: Any) -> GetVideoInfoResp:
        """
        Retrieves metadata and the processing status for an uploaded video.

        Example:
            response = bot.messages.get_video_info(
                video_token="vtok_abc123xyz..."
            )
        """
        req = GetVideoInfoReq(**kwargs)
        path = f"{Paths.VIDEOS}/{req.video_token}"
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", path, GetVideoInfoResp, query=query, payload=payload)

    def answer_callback(self, **kwargs: Any) -> SimpleQueryResult:
        """
        Acknowledges and responds to a user clicking an inline button.

        Example:
            response = bot.messages.answer_callback(
                callback_id="cbk_12345...",
                message=NewMessageBody(text="Action confirmed!")
            )
        """
        req = AnswerCallbackReq(**kwargs)
        query, payload = self.client.split_request(req)
        return self.client.decode("POST", Paths.ANSWERS, SimpleQueryResult, query=query, payload=payload)

    async def get_messages_async(self, **kwargs: Any) -> MessagesList:
        """Async version of get_messages.

        Example:
            # Fetch messages by Chat ID
            response = await bot.messages.get_messages_async(chat_id=123456)
            
            # Fetch specific messages:
            response = await bot.messages.get_messages_async(message_ids=["mid:1", "mid:2"])
        """
        req = GetMessagesReq(**kwargs)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", Paths.MESSAGES, MessagesList, query=query, payload=payload)

    async def send_message_async(self, **kwargs: Any) -> SendMessageResp:
        """
        Async version of send_message.

        Example:
            response = await bot.messages.send_message_async(
                chat_id=123456,
                text="Hello, world!",
                notify=True
            )
        """
        req = SendMessageReq(**kwargs)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("POST", Paths.MESSAGES, SendMessageResp, query=query, payload=payload)

    async def edit_message_async(self, **kwargs: Any) -> SimpleQueryResult:
        """
        Async version of edit_message.

        Example:
            response = await bot.messages.edit_message_async(
                message_id="mid:987654321...",
                text="Updated message text!",
                format="HTML"
            )
        """
        req = EditMessageReq(**kwargs)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("PUT", Paths.MESSAGES, SimpleQueryResult, query=query, payload=payload)

    async def delete_message_async(self, **kwargs: Any) -> SimpleQueryResult:
        """
        Async version of delete_message.

        Example:
            response = await bot.messages.delete_message_async(
                message_id="mid:987654321..."
            )
        """
        req = DeleteMessageReq(**kwargs)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("DELETE", Paths.MESSAGES, SimpleQueryResult, query=query, payload=payload)

    async def get_message_async(self, **kwargs: Any) -> Message:
        """
        Async version of get_message.

        Example:
            response = await bot.messages.get_message_async(
                message_id="mid:987654321..."
            )
        """
        req = GetMessageReq(**kwargs)
        path = f"{Paths.MESSAGES}/{req.message_id}"
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", path, Message, query=query, payload=payload)

    async def get_video_info_async(self, **kwargs: Any) -> GetVideoInfoResp:
        """
        Async version of get_video.

        Example:
            response = await bot.messages.get_video_info_async(
                video_token="vtok_abc123xyz..."
            )
        """
        req = GetVideoInfoReq(**kwargs)
        path = f"{Paths.VIDEOS}/{req.video_token}"
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", path, GetVideoInfoResp, query=query, payload=payload)

    async def answer_callback_async(self, **kwargs: Any) -> SimpleQueryResult:
        """
        Async version of answer_callback.

        Example:
            response = await bot.messages.answer_callback_async(
                callback_id="cbk_12345...",
                message=NewMessageBody(text="Action confirmed!")
            )
        """
        req = AnswerCallbackReq(**kwargs)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("POST", Paths.ANSWERS, SimpleQueryResult, query=query, payload=payload)