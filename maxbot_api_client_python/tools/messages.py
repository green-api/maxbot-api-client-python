from maxbot_api_client_python.client import Client, decode, adecode
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types import models

class Messages:
    def __init__(self, client: Client):
        self.client = client

    def GetMessages(self, **kwargs) -> models.MessagesList:
        """
        Retrieves a list of messages.
        It can fetch messages belonging to a specific ChatID or by an exact list of MessageIDs.

        Example:
            # Fetch messages by Chat ID
            response = api.messages.GetMessages(chat_id=123456)
            
            # Fetch specific messages:
            response = api.messages.GetMessages(message_ids=["mid:1", "mid:2"])
        """
        req = models.GetMessagesReq(**kwargs)
        return decode(self.client, "GET", Paths.MESSAGES, models.MessagesList, query=req.model_dump(exclude_none=True))

    def SendMessage(self, **kwargs) -> models.SendMessageResp:
        """
        Sends a text message or attachment to a specific user or chat.
        If Notify is False, no push notification will be sent to the user.

        Example:
            response = api.messages.SendMessage(
                chat_id=123456,
                text="Hello, world!",
                notify=True
            )
        """
        req = models.SendMessageReq(**kwargs)
        return decode(self.client, "POST", Paths.MESSAGES, models.SendMessageResp, query=req.model_dump(exclude_none=True), payload=req)

    def EditMessage(self, **kwargs) -> models.SimpleQueryResult:
        """
        Modifies the content of a previously sent message.

        Example:
            response = api.messages.EditMessage(
                message_id="mid:987654321...",
                text="Updated message text!",
                format="HTML"
            )
        """
        req = models.EditMessageReq(**kwargs)
        return decode(self.client, "PUT", Paths.MESSAGES, models.SimpleQueryResult, query=req.model_dump(exclude_none=True), payload=req)

    def DeleteMessage(self, **kwargs) -> models.SimpleQueryResult:
        """
        Removes a previously sent message by its ID.

        Example:
            response = api.messages.DeleteMessage(
                message_id="mid:987654321..."
            )
        """
        req = models.DeleteMessageReq(**kwargs)
        return decode(self.client, "DELETE", Paths.MESSAGES, models.SimpleQueryResult, query=req.model_dump(exclude_none=True))

    def GetMessage(self, **kwargs) -> models.Message:
        """
        Retrieves full information about a message by its ID.

        Example:
            response = api.messages.GetMessage(
                message_id="mid:987654321..."
            )
        """
        req = models.GetMessageReq(**kwargs)
        path = f"{Paths.MESSAGES}/{req.message_id}"
        return decode(self.client, "GET", path, models.Message)

    def GetVideoInfo(self, **kwargs) -> models.GetVideoInfoResp:
        """
        Retrieves metadata and the processing status for an uploaded video.

        Example:
            response = api.messages.GetVideoInfo(
                video_token="vtok_abc123xyz..."
            )
        """
        req = models.GetVideoInfoReq(**kwargs)
        path = f"{Paths.VIDEOS}/{req.video_token}"
        return decode(self.client, "GET", path, models.GetVideoInfoResp)

    def AnswerCallback(self, **kwargs) -> models.SimpleQueryResult:
        """
        Acknowledges and responds to a user clicking an inline button.

        Example:
            response = api.messages.AnswerCallback(
                callback_id="cbk_12345...",
                message=NewMessageBody(text="Action confirmed!")
            )
        """
        req = models.AnswerCallbackReq(**kwargs)
        return decode(self.client, "POST", Paths.ANSWERS, models.SimpleQueryResult, query=req.model_dump(exclude_none=True), payload=req)

    async def GetMessagesAsync(self, **kwargs) -> models.MessagesList:
        """Async version of GetMessages.

        Example:
            # Fetch messages by Chat ID
            response = await api.messages.GetMessagesAsync(chat_id=123456)
            
            # Fetch specific messages:
            response = await api.messages.GetMessagesAsync(message_ids=["mid:1", "mid:2"])
        """
        req = models.GetMessagesReq(**kwargs)
        return await adecode(self.client, "GET", Paths.MESSAGES, models.MessagesList, query=req.model_dump(exclude_none=True))

    async def SendMessageAsync(self, **kwargs) -> models.SendMessageResp:
        """
        Async version of SendMessage.

        Example:
            response = await api.messages.SendMessageAsync(
                chat_id=123456,
                text="Hello, world!",
                notify=True
            )
        """
        req = models.SendMessageReq(**kwargs)
        return await adecode(self.client, "POST", Paths.MESSAGES, models.SendMessageResp, query=req.model_dump(exclude_none=True), payload=req)

    async def EditMessageAsync(self, **kwargs) -> models.SimpleQueryResult:
        """
        Async version of EditMessage.

        Example:
            response = await api.messages.EditMessageAsync(
                message_id="mid:987654321...",
                text="Updated message text!",
                format="HTML"
            )
        """
        req = models.EditMessageReq(**kwargs)
        return await adecode(self.client, "PUT", Paths.MESSAGES, models.SimpleQueryResult, query=req.model_dump(exclude_none=True), payload=req)

    async def DeleteMessageAsync(self, **kwargs) -> models.SimpleQueryResult:
        """
        Async version of DeleteMessage.

        Example:
            response = await api.messages.DeleteMessageAsync(
                message_id="mid:987654321..."
            )
        """
        req = models.DeleteMessageReq(**kwargs)
        return await adecode(self.client, "DELETE", Paths.MESSAGES, models.SimpleQueryResult, query=req.model_dump(exclude_none=True))

    async def GetMessageAsync(self, **kwargs) -> models.Message:
        """
        Async version of GetMessage.

        Example:
            response = await api.messages.GetMessageAsync(
                message_id="mid:987654321..."
            )
        """
        req = models.GetMessageReq(**kwargs)
        path = f"{Paths.MESSAGES}/{req.message_id}"
        return await adecode(self.client, "GET", path, models.Message)

    async def GetVideoInfoAsync(self, **kwargs) -> models.GetVideoInfoResp:
        """
        Async version of GetVideoInfo.

        Example:
            response = await api.messages.GetVideoInfoAsync(
                video_token="vtok_abc123xyz..."
            )
        """
        req = models.GetVideoInfoReq(**kwargs)
        path = f"{Paths.VIDEOS}/{req.video_token}"
        return await adecode(self.client, "GET", path, models.GetVideoInfoResp)

    async def AnswerCallbackAsync(self, **kwargs) -> models.SimpleQueryResult:
        """
        Async version of AnswerCallback.

        Example:
            response = await api.messages.AnswerCallbackAsync(
                callback_id="cbk_12345...",
                message=NewMessageBody(text="Action confirmed!")
            )
        """
        req = models.AnswerCallbackReq(**kwargs)
        return await adecode(self.client, "POST", Paths.ANSWERS, models.SimpleQueryResult, query=req.model_dump(exclude_none=True), payload=req)