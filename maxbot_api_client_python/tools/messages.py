from maxbot_api_client_python.client import Client, decode, adecode
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types.models import *

class Messages:
    def __init__(self, client: Client):
        self.client = client

    def GetMessages(self, req: GetMessagesReq) -> MessagesList:
        """
        Retrieves a list of messages.
        It can fetch messages belonging to a specific ChatID or by an exact list of MessageIDs.

        Example:
            # Fetch messages by Chat ID
            response = api.messages.GetMessages(GetMessagesReq(chat_id=123456))
            
            # Fetch specific messages:
            response = api.messages.GetMessages(GetMessagesReq(message_ids=["mid:1", "mid:2"]))
        """
        return decode(self.client, "GET", Paths.MESSAGES, MessagesList, query=req.model_dump(exclude_none=True))

    def SendMessage(self, req: SendMessageReq) -> SendMessageResp:
        """
        Sends a text message or attachment to a specific user or chat.
        If Notify is False, no push notification will be sent to the user.

        Example:
            response = api.messages.SendMessage(SendMessageReq(
                chat_id=123456,
                text="Hello, world!",
                notify=True
            ))
        """
        return decode(self.client, "POST", Paths.MESSAGES, SendMessageResp, query=req.model_dump(exclude_none=True), payload=req)

    def EditMessage(self, req: EditMessageReq) -> SimpleQueryResult:
        """
        Modifies the content of a previously sent message.

        Example:
            response = api.messages.EditMessage(EditMessageReq(
                message_id="mid:987654321...",
                text="Updated message text!",
                format="HTML"
            ))
        """
        return decode(self.client, "PUT", Paths.MESSAGES, SimpleQueryResult, query=req.model_dump(exclude_none=True), payload=req)

    def DeleteMessage(self, req: DeleteMessageReq) -> SimpleQueryResult:
        """
        Removes a previously sent message by its ID.

        Example:
            response = api.messages.DeleteMessage(DeleteMessageReq(
                message_id="mid:987654321..."
            ))
        """
        return decode(self.client, "DELETE", Paths.MESSAGES, SimpleQueryResult, query=req.model_dump(exclude_none=True))

    def GetMessage(self, req: GetMessageReq) -> Message:
        """
        Retrieves full information about a message by its ID.

        Example:
            response = api.messages.GetMessage(GetMessageReq(
                message_id="mid:987654321..."
            ))
        """
        path = f"{Paths.MESSAGES}/{req.message_id}"
        return decode(self.client, "GET", path, Message)

    def GetVideoInfo(self, req: GetVideoInfoReq) -> GetVideoInfoResp:
        """
        Retrieves metadata and the processing status for an uploaded video.

        Example:
            response = api.messages.GetVideoInfo(GetVideoInfoReq(
                video_token="vtok_abc123xyz..."
            ))
        """
        path = f"{Paths.VIDEOS}/{req.video_token}"
        return decode(self.client, "GET", path, GetVideoInfoResp)

    def AnswerCallback(self, req: AnswerCallbackReq) -> SimpleQueryResult:
        """
        Acknowledges and responds to a user clicking an inline button.

        Example:
            response = api.messages.AnswerCallback(AnswerCallbackReq(
                callback_id="cbk_12345...",
                message=NewMessageBody(text="Action confirmed!")
            ))
        """
        return decode(self.client, "POST", Paths.ANSWERS, SimpleQueryResult, query=req.model_dump(exclude_none=True), payload=req)

    async def GetMessagesAsync(self, req: GetMessagesReq) -> MessagesList:
        """Async version of GetMessages.

        Example:
            # Fetch messages by Chat ID
            response = await api.messages.GetMessagesAsync(GetMessagesReq(chat_id=123456))
            
            # Fetch specific messages:
            response = await api.messages.GetMessagesAsync(GetMessagesReq(message_ids=["mid:1", "mid:2"]))
        """
        return await adecode(self.client, "GET", Paths.MESSAGES, MessagesList, query=req.model_dump(exclude_none=True))

    async def SendMessageAsync(self, req: SendMessageReq) -> SendMessageResp:
        """
        Async version of SendMessage.

        Example:
            response = await api.messages.SendMessageAsync(SendMessageReq(
                chat_id=123456,
                text="Hello, world!",
                notify=True
            ))
        """
        return await adecode(self.client, "POST", Paths.MESSAGES, SendMessageResp, query=req.model_dump(exclude_none=True), payload=req)

    async def EditMessageAsync(self, req: EditMessageReq) -> SimpleQueryResult:
        """
        Async version of EditMessage.

        Example:
            response = await api.messages.EditMessageAsync(EditMessageReq(
                message_id="mid:987654321...",
                text="Updated message text!",
                format="HTML"
            ))
        """
        return await adecode(self.client, "PUT", Paths.MESSAGES, SimpleQueryResult, query=req.model_dump(exclude_none=True), payload=req)

    async def DeleteMessageAsync(self, req: DeleteMessageReq) -> SimpleQueryResult:
        """
        Async version of DeleteMessage.

        Example:
            response = await api.messages.DeleteMessageAsync(DeleteMessageReq(
                message_id="mid:987654321..."
            ))
        """
        return await adecode(self.client, "DELETE", Paths.MESSAGES, SimpleQueryResult, query=req.model_dump(exclude_none=True))

    async def GetMessageAsync(self, req: GetMessageReq) -> Message:
        """
        Async version of GetMessage.

        Example:
            response = await api.messages.GetMessageAsync(GetMessageReq(
                message_id="mid:987654321..."
            ))
        """
        path = f"{Paths.MESSAGES}/{req.message_id}"
        return await adecode(self.client, "GET", path, Message)

    async def GetVideoInfoAsync(self, req: GetVideoInfoReq) -> GetVideoInfoResp:
        """
        Async version of GetVideoInfo.

        Example:
            response = await api.messages.GetVideoInfoAsync(GetVideoInfoReq(
                video_token="vtok_abc123xyz..."
            ))
        """
        path = f"{Paths.VIDEOS}/{req.video_token}"
        return await adecode(self.client, "GET", path, GetVideoInfoResp)

    async def AnswerCallbackAsync(self, req: AnswerCallbackReq) -> SimpleQueryResult:
        """
        Async version of AnswerCallback.

        Example:
            response = await api.messages.AnswerCallbackAsync(AnswerCallbackReq(
                callback_id="cbk_12345...",
                message=NewMessageBody(text="Action confirmed!")
            ))
        """
        return await adecode(self.client, "POST", Paths.ANSWERS, SimpleQueryResult, query=req.model_dump(exclude_none=True), payload=req)