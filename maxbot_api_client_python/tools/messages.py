from typing import Any

from maxbot_api_client_python.client import Client
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types.models import (
    AnswerCallbackReq, DeleteMessageReq, EditMessageReq, GetMessageReq, GetMessagesReq, 
    GetVideoInfoReq, GetVideoInfoResp, Message, MessagesList, SendMessageReq, 
    SendMessageResp, SimpleQueryResult, NewMessageBody
)

class Messages:
    def __init__(self, client: Client):
        self.client = client

    def get_messages(self, req: GetMessagesReq) -> MessagesList:
        """
        Retrieves a list of messages.
        It can fetch messages belonging to a specific ChatID or by an exact list of MessageIDs.

        Example:
            # Fetch messages by Chat ID
            response = bot.messages.get_messages(GetMessagesReq(chat_id=123456))
            
            # Fetch specific messages:
            response = bot.messages.get_messages(GetMessagesReq(message_ids=["mid:1", "mid:2"]))
        """
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", Paths.MESSAGES, MessagesList, query=query, payload=payload)

    def send_message(self, req: SendMessageReq) -> SendMessageResp:
        """
        Sends a text message or attachment to a specific user or chat.
        If Notify is False, no push notification will be sent to the user.

        Example:
            response = bot.messages.send_message(SendMessageReq(
                chat_id=123456,
                text="Hello, world!",
                notify=True
            ))
        """
        query, payload = self.client.split_request(req)
        return self.client.decode("POST", Paths.MESSAGES, SendMessageResp, query=query, payload=payload)

    def edit_message(self, req: EditMessageReq) -> SimpleQueryResult:
        """
        Modifies the content of a previously sent message.

        Example:
            response = bot.messages.edit_message(EditMessageReq(
                message_id="mid:987654321...",
                text="Updated message text!",
                format="HTML"
            ))
        """
        query, payload = self.client.split_request(req)
        return self.client.decode("PUT", Paths.MESSAGES, SimpleQueryResult, query=query, payload=payload)

    def delete_message(self, req: DeleteMessageReq) -> SimpleQueryResult:
        """
        Removes a previously sent message by its ID.

        Example:
            response = bot.messages.delete_message(DeleteMessageReq(
                message_id="mid:987654321..."
            ))
        """
        query, payload = self.client.split_request(req)
        return self.client.decode("DELETE", Paths.MESSAGES, SimpleQueryResult, query=query, payload=payload)

    def get_message(self, req: GetMessageReq) -> Message:
        """
        Retrieves full information about a message by its ID.

        Example:
            response = bot.messages.get_message(GetMessageReq(
                message_id="mid:987654321..."
            ))
        """
        path = f"{Paths.MESSAGES}/{req.message_id}"
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", path, Message, query=query, payload=payload)

    def get_video_info(self, req: GetVideoInfoReq) -> GetVideoInfoResp:
        """
        Retrieves metadata and the processing status for an uploaded video.

        Example:
            response = bot.messages.get_video_info(GetVideoInfoReq(
                video_token="vtok_abc123xyz..."
            ))
        """
        path = f"{Paths.VIDEOS}/{req.video_token}"
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", path, GetVideoInfoResp, query=query, payload=payload)

    def answer_callback(self, req: AnswerCallbackReq) -> SimpleQueryResult:
        """
        Acknowledges and responds to a user clicking an inline button.

        Example:
            response = bot.messages.answer_callback(AnswerCallbackReq(
                callback_id="cbk_12345...",
                message=NewMessageBody(text="Action confirmed!")
            ))
        """
        query, payload = self.client.split_request(req)
        return self.client.decode("POST", Paths.ANSWERS, SimpleQueryResult, query=query, payload=payload)

    async def get_messages_async(self, req: GetMessagesReq) -> MessagesList:
        """Async version of get_messages.

        Example:
            # Fetch messages by Chat ID
            response = await bot.messages.get_messages_async(GetMessagesReq(chat_id=123456))
            
            # Fetch specific messages:
            response = await bot.messages.get_messages_async(GetMessagesReq(message_ids=["mid:1", "mid:2"]))
        """
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", Paths.MESSAGES, MessagesList, query=query, payload=payload)

    async def send_message_async(self, req: SendMessageReq) -> SendMessageResp:
        """
        Async version of send_message.

        Example:
            response = await bot.messages.send_message_async(SendMessageReq(
                chat_id=123456,
                text="Hello, world!",
                notify=True
            ))
        """
        query, payload = self.client.split_request(req)
        return await self.client.adecode("POST", Paths.MESSAGES, SendMessageResp, query=query, payload=payload)

    async def edit_message_async(self, req: EditMessageReq) -> SimpleQueryResult:
        """
        Async version of edit_message.

        Example:
            response = await bot.messages.edit_message_async(EditMessageReq(
                message_id="mid:987654321...",
                text="Updated message text!",
                format="HTML"
            ))
        """
        query, payload = self.client.split_request(req)
        return await self.client.adecode("PUT", Paths.MESSAGES, SimpleQueryResult, query=query, payload=payload)

    async def delete_message_async(self, req: DeleteMessageReq) -> SimpleQueryResult:
        """
        Async version of delete_message.

        Example:
            response = await bot.messages.delete_message_async(DeleteMessageReq(
                message_id="mid:987654321..."
            ))
        """
        query, payload = self.client.split_request(req)
        return await self.client.adecode("DELETE", Paths.MESSAGES, SimpleQueryResult, query=query, payload=payload)

    async def get_message_async(self, req: GetMessageReq) -> Message:
        """
        Async version of get_message.

        Example:
            response = await bot.messages.get_message_async(GetMessageReq(
                message_id="mid:987654321..."
            ))
        """
        path = f"{Paths.MESSAGES}/{req.message_id}"
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", path, Message, query=query, payload=payload)

    async def get_video_info_async(self, req: GetVideoInfoReq) -> GetVideoInfoResp:
        """
        Async version of get_video.

        Example:
            response = await bot.messages.get_video_info_async(GetVideoInfoReq(
                video_token="vtok_abc123xyz..."
            ))
        """
        path = f"{Paths.VIDEOS}/{req.video_token}"
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", path, GetVideoInfoResp, query=query, payload=payload)

    async def answer_callback_async(self, req: AnswerCallbackReq) -> SimpleQueryResult:
        """
        Async version of answer_callback.

        Example:
            response = await bot.messages.answer_callback_async(AnswerCallbackReq(
                callback_id="cbk_12345...",
                message=NewMessageBody(text="Action confirmed!")
            ))
        """
        query, payload = self.client.split_request(req)
        return await self.client.adecode("POST", Paths.ANSWERS, SimpleQueryResult, query=query, payload=payload)