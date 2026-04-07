from maxbot_api_client_python.client import Client, decode, adecode
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types import models

class Chats:
    def __init__(self, client: Client):
        self.client = client

    def GetChats(self, **kwargs) -> models.GetChatsResp:
        """
        Returns information about chats that the bot participated in: a result list and a marker pointing to the next page.

        Example:
            response = api.chats.GetChats(
                count=20
            )
        """
        req = models.GetChatsReq(**kwargs)
        return decode(self.client, "GET", Paths.CHATS, models.GetChatsResp, query=req.model_dump(exclude_none=True))

    def GetChat(self, **kwargs) -> models.ChatInfo:
        """
        Returns info about a specific chat.

        Example:
            response = api.chats.GetChat(
                chat_id=123456789
            )
        """
        req = models.GetChatReq(**kwargs)
        path = Paths.CHATS_ID.format(req.chat_id)
        return decode(self.client, "GET", path, models.ChatInfo)

    def EditChat(self, **kwargs) -> models.ChatInfo:
        """
        Modifies the properties of a chat, such as its title, icon, or notification settings.

        Example:
            response = api.chats.EditChat(
                chat_id=123456789,
                title="Updated Chat Title",
                notify=True
            )
        """
        req = models.EditChatReq(**kwargs)
        path = Paths.CHATS_ID.format(req.chat_id)
        return decode(self.client, "PATCH", path, models.ChatInfo, payload=req)

    def DeleteChat(self, **kwargs) -> models.SimpleQueryResult:
        """
        Permanently deletes a chat for the bot.

        Example:
            response = api.chats.DeleteChat(
                chat_id=123456789
            )
        """
        req = models.DeleteChatReq(**kwargs)
        path = Paths.CHATS_ID.format(req.chat_id)
        return decode(self.client, "DELETE", path, models.SimpleQueryResult)

    def SendAction(self, **kwargs) -> models.SimpleQueryResult:
        """
        Broadcasts a temporary status action (e.g., "typing...", "recording video...") to the chat participants.

        Example:
            response = api.chats.SendAction(
                chat_id=123456789,
                action="mark_seen"
            )
        """
        req = models.SendActionReq(**kwargs)
        path = Paths.CHATS_ACTIONS.format(req.chat_id)
        return decode(self.client, "POST", path, models.SimpleQueryResult, payload=req)

    def GetPinnedMessage(self, **kwargs) -> models.Message:
        """
        Retrieves the currently pinned message in the specified chat.

        Example:
            response = api.chats.GetPinnedMessage(
                chat_id=123456789
            )
        """
        req = models.GetPinnedMessageReq(**kwargs)
        path = Paths.CHATS_PIN.format(req.chat_id)
        return decode(self.client, "GET", path, models.Message)

    def PinMessage(self, **kwargs) -> models.SimpleQueryResult:
        """
        Pins a specific message in the chat.
        You can optionally specify whether to notify chat members about the new pinned message.

        Example:
            response = api.chats.PinMessage(
                chat_id=123456789,
                message_id="mid:987654321...",
                notify=True
            )
        """
        req = models.PinMessageReq(**kwargs)
        path = Paths.CHATS_PIN.format(req.chat_id)
        return decode(self.client, "PUT", path, models.SimpleQueryResult, payload=req)

    def UnpinMessage(self, **kwargs) -> models.SimpleQueryResult:
        """
        Removes the pinned message from the specified chat.

        Example:
            response = api.chats.UnpinMessage(
                chat_id=123456789
            )
        """
        req = models.UnpinMessageReq(**kwargs)
        path = Paths.CHATS_PIN.format(req.chat_id)
        return decode(self.client, "DELETE", path, models.SimpleQueryResult)

    def GetChatMembership(self, **kwargs) -> models.ChatMember:
        """
        Returns chat membership info for the current bot.

        Example:
            response = api.chats.GetChatMembership(
                chat_id=123456789
            )
        """
        req = models.GetChatMembershipReq(**kwargs)
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        return decode(self.client, "GET", path, models.ChatMember)

    def LeaveChat(self, **kwargs) -> models.SimpleQueryResult:
        """
        Removes the bot from chat members.

        Example:
            response = api.chats.LeaveChat(
                chat_id=123456789
            )
        """
        req = models.LeaveChatReq(**kwargs)
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        return decode(self.client, "DELETE", path, models.SimpleQueryResult)

    def GetChatAdmins(self, **kwargs) -> models.GetChatAdminsResp:
        """
        Retrieves a list of administrators for the specified group chat.

        Example:
            response = api.chats.GetChatAdmins(
                chat_id=123456789
            )
        """
        req = models.GetChatAdminsReq(**kwargs)
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        return decode(self.client, "GET", path, models.GetChatAdminsResp)

    def SetChatAdmins(self, **kwargs) -> models.SimpleQueryResult:
        """
        Assigns administrator rights to specific users in a group chat.

        Example:
            response = api.chats.SetChatAdmins(
                chat_id=123456789,
                admins=[
                    ChatAdmin(user_id=98765, role="admin"),
                    ChatAdmin(user_id=43210, role="admin")
                ]
            )
        """
        req = models.SetChatAdminsReq(**kwargs)
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        return decode(self.client, "POST", path, models.SimpleQueryResult, payload=req)

    def DeleteAdmin(self, **kwargs) -> models.SimpleQueryResult:
        """
        Revokes administrator rights from a specific user in a group chat.

        Example:
            response = api.chats.DeleteAdmin(
                chat_id=123456789,
                user_id=98765
            )
        """
        req = models.DeleteAdminReq(**kwargs)
        path = Paths.CHATS_MEMBERS_ADMIN_ID.format(req.chat_id, req.user_id)
        return decode(self.client, "DELETE", path, models.SimpleQueryResult)

    def GetChatMembers(self, **kwargs) -> models.GetChatAdminsResp:
        """
        Returns users participated in the chat.

        Example:
            response = api.chats.GetChatMembers(
                chat_id=123456789,
                count=20
            )
        """
        req = models.GetChatMembersReq(**kwargs)
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return decode(self.client, "GET", path, models.GetChatAdminsResp, query=req.model_dump(exclude_none=True))

    def AddMembers(self, **kwargs) -> models.AddMembersResp:
        """
        Adds one or more users to a group chat.

        Example:
            response = api.chats.AddMembers(
                chat_id=123456789,
                user_ids=[11111, 22222]
            )
        """
        req = models.AddMembersReq(**kwargs)
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return decode(self.client, "POST", path, models.AddMembersResp, payload=req)

    def DeleteMember(self, **kwargs) -> models.SimpleQueryResult:
        """
        Removes a specific user from a group chat.
        You can optionally block the user from rejoining.

        Example:
            response = api.chats.DeleteMember(
                chat_id=123456789,
                user_id=98765,
                block=True
            )
        """
        req = models.DeleteMemberReq(**kwargs)
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return decode(self.client, "DELETE", path, models.SimpleQueryResult, query=req.model_dump(exclude_none=True))

    async def GetChatsAsync(self, **kwargs) -> models.GetChatsResp:
        """
        Async version of GetChats.

        Example:
            response = await api.chats.GetChatsAsync(
                count=20
            )
        """
        req = models.GetChatsReq(**kwargs)
        return await adecode(self.client, "GET", Paths.CHATS, models.GetChatsResp, query=req.model_dump(exclude_none=True))

    async def GetChatAsync(self, **kwargs) -> models.ChatInfo:
        """
        Async version of GetChat.

        Example:
            response = await api.chats.GetChatAsync(
                chat_id=123456789
            )
        """
        req = models.GetChatReq(**kwargs)
        path = Paths.CHATS_ID.format(req.chat_id)
        return await adecode(self.client, "GET", path, models.ChatInfo)

    async def EditChatAsync(self, **kwargs) -> models.ChatInfo:
        """
        Async version of EditChat.

        Example:
            response = await api.chats.EditChatAsync(
                chat_id=123456789,
                title="Updated Chat Title"
            )
        """
        req = models.EditChatReq(**kwargs)
        path = Paths.CHATS_ID.format(req.chat_id)
        return await adecode(self.client, "PATCH", path, models.ChatInfo, payload=req)

    async def DeleteChatAsync(self, **kwargs) -> models.SimpleQueryResult:
        """
        Async version of DeleteChat.

        Example:
            response = await api.chats.DeleteChatAsync(
                chat_id=123456789
            )
        """
        req = models.DeleteChatReq(**kwargs)
        path = Paths.CHATS_ID.format(req.chat_id)
        return await adecode(self.client, "DELETE", path, models.SimpleQueryResult)

    async def SendActionAsync(self, **kwargs) -> models.SimpleQueryResult:
        """
        Async version of SendAction.

        Example:
            response = await api.chats.SendActionAsync(
                chat_id=123456789,
                action="typing"
            )
        """
        req = models.SendActionReq(**kwargs)
        path = Paths.CHATS_ACTIONS.format(req.chat_id)
        return await adecode(self.client, "POST", path, models.SimpleQueryResult, payload=req)

    async def GetPinnedMessageAsync(self, **kwargs) -> models.Message:
        """
        Async version of GetPinnedMessage.

        Example:
            response = await api.chats.GetPinnedMessageAsync(
                chat_id=123456789
            )
        """
        req = models.GetPinnedMessageReq(**kwargs)
        path = Paths.CHATS_PIN.format(req.chat_id)
        return await adecode(self.client, "GET", path, models.Message)

    async def PinMessageAsync(self, **kwargs) -> models.SimpleQueryResult:
        """
        Async version of PinMessage.

        Example:
            response = await api.chats.PinMessageAsync(
                chat_id=123456789,
                message_id="mid:987654321..."
            )
        """
        req = models.PinMessageReq(**kwargs)
        path = Paths.CHATS_PIN.format(req.chat_id)
        return await adecode(self.client, "PUT", path, models.SimpleQueryResult, payload=req)

    async def UnpinMessageAsync(self, **kwargs) -> models.SimpleQueryResult:
        """
        Async version of UnpinMessage.

        Example:
            response = await api.chats.UnpinMessageAsync(
                chat_id=123456789
            )
        """
        req = models.UnpinMessageReq(**kwargs)
        path = Paths.CHATS_PIN.format(req.chat_id)
        return await adecode(self.client, "DELETE", path, models.SimpleQueryResult)

    async def GetChatMembershipAsync(self, **kwargs) -> models.ChatMember:
        """
        Async version of GetChatMembership.

        Example:
            response = await api.chats.GetChatMembershipAsync(
                chat_id=123456789
            )
        """
        req = models.GetChatMembershipReq(**kwargs)
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        return await adecode(self.client, "GET", path, models.ChatMember)

    async def LeaveChatAsync(self, **kwargs) -> models.SimpleQueryResult:
        """
        Async version of LeaveChat.

        Example:
            response = await api.chats.LeaveChatAsync(
                chat_id=123456789
            )
        """
        req = models.LeaveChatReq(**kwargs)
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        return await adecode(self.client, "DELETE", path, models.SimpleQueryResult)

    async def GetChatAdminsAsync(self, **kwargs) -> models.GetChatAdminsResp:
        """
        Async version of GetChatAdmins.

        Example:
            response = await api.chats.GetChatAdminsAsync(
                chat_id=123456789
            )
        """
        req = models.GetChatAdminsReq(**kwargs)
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        return await adecode(self.client, "GET", path, models.GetChatAdminsResp)

    async def SetChatAdminsAsync(self, **kwargs) -> models.SimpleQueryResult:
        """
        Async version of SetChatAdmins.

        Example:
            response = await api.chats.SetChatAdminsAsync(
                chat_id=123456789,
                admins=[ChatAdmin(user_id=98765, role="admin")]
            )
        """
        req = models.SetChatAdminsReq(**kwargs)
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        return await adecode(self.client, "POST", path, models.SimpleQueryResult, payload=req)

    async def DeleteAdminAsync(self, **kwargs) -> models.SimpleQueryResult:
        """
        Async version of DeleteAdmin.

        Example:
            response = await api.chats.DeleteAdminAsync(
                chat_id=123456789,
                user_id=98765
            )
        """
        req = models.DeleteAdminReq(**kwargs)
        path = Paths.CHATS_MEMBERS_ADMIN_ID.format(req.chat_id, req.user_id)
        return await adecode(self.client, "DELETE", path, models.SimpleQueryResult)

    async def GetChatMembersAsync(self, **kwargs) -> models.GetChatAdminsResp:
        """
        Async version of GetChatMembers.

        Example:
            response = await api.chats.GetChatMembersAsync(
                chat_id=123456789,
                count=20
            )
        """
        req = models.GetChatMembersReq(**kwargs)
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return await adecode(self.client, "GET", path, models.GetChatAdminsResp, query=req.model_dump(exclude_none=True))

    async def AddMembersAsync(self, **kwargs) -> models.AddMembersResp:
        """
        Async version of AddMembers.

        Example:
            response = await api.chats.AddMembersAsync(
                chat_id=123456789,
                user_ids=[11111, 22222]
            )
        """
        req = models.AddMembersReq(**kwargs)
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return await adecode(self.client, "POST", path, models.AddMembersResp, payload=req)

    async def DeleteMemberAsync(self, **kwargs) -> models.SimpleQueryResult:
        """
        Async version of DeleteMember.

        Example:
            response = await api.chats.DeleteMemberAsync(
                chat_id=123456789,
                user_id=98765
            )
        """
        req = models.DeleteMemberReq(**kwargs)
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return await adecode(self.client, "DELETE", path, models.SimpleQueryResult, query=req.model_dump(exclude_none=True))