from maxbot_api_client_python.client import Client, decode, adecode
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types import models

class Chats:
    def __init__(self, client: Client):
        self.client = client

    def GetChats(self, req: models.GetChatsReq) ->  models.GetChatsResp:
        """
        Returns information about chats that the bot participated in: a result list and a marker pointing to the next page.

        Example:
            response = api.chats.GetChats(GetChatsReq(
                count=20
            ))
        """
        return decode(self.client, "GET", Paths.CHATS,  models.GetChatsResp, query=req.model_dump(exclude_none=True))

    def GetChat(self, req:  models.GetChatReq) ->  models.ChatInfo:
        """
        Returns info about a specific chat.

        Example:
            response = api.chats.GetChat(GetChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        return decode(self.client, "GET", path,  models.ChatInfo)

    def EditChat(self, req:  models.EditChatReq) ->  models.ChatInfo:
        """
        Modifies the properties of a chat, such as its title, icon, or notification settings.

        Example:
            response = api.chats.EditChat(EditChatReq(
                chat_id=123456789,
                title="Updated Chat Title",
                notify=True
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        return decode(self.client, "PATCH", path,  models.ChatInfo, payload=req)

    def DeleteChat(self, req:  models.DeleteChatReq) ->  models.SimpleQueryResult:
        """
        Permanently deletes a chat for the bot.

        Example:
            response = api.chats.DeleteChat(DeleteChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        return decode(self.client, "DELETE", path,  models.SimpleQueryResult)

    def SendAction(self, req:  models.SendActionReq) ->  models.SimpleQueryResult:
        """
        Broadcasts a temporary status action (e.g., "typing...", "recording video...") to the chat participants.

        Example:
            response = api.chats.SendAction(SendActionReq(
                chat_id=123456789,
                action="mark_seen"
            ))
        """
        path = Paths.CHATS_ACTIONS.format(req.chat_id)
        return decode(self.client, "POST", path,  models.SimpleQueryResult, payload=req)

    def GetPinnedMessage(self, req:  models.GetPinnedMessageReq) ->  models.Message:
        """
        Retrieves the currently pinned message in the specified chat.

        Example:
            response = api.chats.GetPinnedMessage(GetPinnedMessageReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        return decode(self.client, "GET", path,  models.Message)

    def PinMessage(self, req:  models.PinMessageReq) ->  models.SimpleQueryResult:
        """
        Pins a specific message in the chat.
        You can optionally specify whether to notify chat members about the new pinned message.

        Example:
            response = api.chats.PinMessage(PinMessageReq(
                chat_id=123456789,
                message_id="mid:987654321...",
                notify=True
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        return decode(self.client, "PUT", path,  models.SimpleQueryResult, payload=req)

    def UnpinMessage(self, req:  models.UnpinMessageReq) ->  models.SimpleQueryResult:
        """
        Removes the pinned message from the specified chat.

        Example:
            response = api.chats.UnpinMessage(UnpinMessageReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        return decode(self.client, "DELETE", path,  models.SimpleQueryResult)

    def GetChatMembership(self, req:  models.GetChatMembershipReq) ->  models.ChatMember:
        """
        Returns chat membership info for the current bot.

        Example:
            response = api.chats.GetChatMembership(GetChatMembershipReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        return decode(self.client, "GET", path,  models.ChatMember)

    def LeaveChat(self, req:  models.LeaveChatReq) ->  models.SimpleQueryResult:
        """
        Removes the bot from chat members.

        Example:
            response = api.chats.LeaveChat(LeaveChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        return decode(self.client, "DELETE", path,  models.SimpleQueryResult)

    def GetChatAdmins(self, req:  models.GetChatAdminsReq) ->  models.GetChatAdminsResp:
        """
        Retrieves a list of administrators for the specified group chat.

        Example:
            response = api.chats.GetChatAdmins(GetChatAdminsReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        return decode(self.client, "GET", path,  models.GetChatAdminsResp)

    def SetChatAdmins(self, req:  models.SetChatAdminsReq) ->  models.SimpleQueryResult:
        """
        Assigns administrator rights to specific users in a group chat.

        Example:
            response = api.chats.SetChatAdmins(SetChatAdminsReq(
                chat_id=123456789,
                admins=[
                    ChatAdmin(user_id=98765, role="admin"),
                    ChatAdmin(user_id=43210, role="admin")
                ]
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        return decode(self.client, "POST", path,  models.SimpleQueryResult, payload=req)

    def DeleteAdmin(self, req:  models.DeleteAdminReq) ->  models.SimpleQueryResult:
        """
        Revokes administrator rights from a specific user in a group chat.

        Example:
            response = api.chats.DeleteAdmin(DeleteAdminReq(
                chat_id=123456789,
                user_id=98765
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN_ID.format(req.chat_id, req.user_id)
        return decode(self.client, "DELETE", path,  models.SimpleQueryResult)

    def GetChatMembers(self, req:  models.GetChatMembersReq) ->  models.GetChatAdminsResp:
        """
        Returns users participated in the chat.

        Example:
            response = api.chats.GetChatMembers(GetChatMembersReq(
                chat_id=123456789,
                count=20
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return decode(self.client, "GET", path,  models.GetChatAdminsResp, query=req.model_dump(exclude_none=True))

    def AddMembers(self, req:  models.AddMembersReq) ->  models.AddMembersResp:
        """
        Adds one or more users to a group chat.

        Example:
            response = api.chats.AddMembers(AddMembersReq(
                chat_id=123456789,
                user_ids=[11111, 22222]
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return decode(self.client, "POST", path,  models.AddMembersResp, payload=req)

    def DeleteMember(self, req:  models.DeleteMemberReq) ->  models.SimpleQueryResult:
        """
        Removes a specific user from a group chat.
        You can optionally block the user from rejoining.

        Example:
            response = api.chats.DeleteMember(DeleteMemberReq(
                chat_id=123456789,
                user_id=98765,
                block=True
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return decode(self.client, "DELETE", path,  models.SimpleQueryResult, query=req.model_dump(exclude_none=True))

    async def GetChatsAsync(self, req:  models.GetChatsReq) ->  models.GetChatsResp:
        """
        Async version of GetChats.

        Example:
            response = await api.chats.GetChatsAsync(GetChatsReq(
                count=20
            ))
        """
        return await adecode(self.client, "GET", Paths.CHATS,  models.GetChatsResp, query=req.model_dump(exclude_none=True))

    async def GetChatAsync(self, req:  models.GetChatReq) ->  models.ChatInfo:
        """
        Async version of GetChat.

        Example:
            response = await api.chats.GetChatAsync(GetChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        return await adecode(self.client, "GET", path,  models.ChatInfo)

    async def EditChatAsync(self, req:  models.EditChatReq) ->  models.ChatInfo:
        """
        Async version of EditChat.

        Example:
            response = await api.chats.EditChatAsync(EditChatReq(
                chat_id=123456789,
                title="Updated Chat Title"
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        return await adecode(self.client, "PATCH", path,  models.ChatInfo, payload=req)

    async def DeleteChatAsync(self, req:  models.DeleteChatReq) ->  models.SimpleQueryResult:
        """
        Async version of DeleteChat.

        Example:
            response = await api.chats.DeleteChatAsync(DeleteChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        return await adecode(self.client, "DELETE", path,  models.SimpleQueryResult)

    async def SendActionAsync(self, req:  models.SendActionReq) ->  models.SimpleQueryResult:
        """
        Async version of SendAction.

        Example:
            response = await api.chats.SendActionAsync(SendActionReq(
                chat_id=123456789,
                action="typing"
            ))
        """
        path = Paths.CHATS_ACTIONS.format(req.chat_id)
        return await adecode(self.client, "POST", path,  models.SimpleQueryResult, payload=req)

    async def GetPinnedMessageAsync(self, req:  models.GetPinnedMessageReq) ->  models.Message:
        """
        Async version of GetPinnedMessage.

        Example:
            response = await api.chats.GetPinnedMessageAsync(GetPinnedMessageReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        return await adecode(self.client, "GET", path,  models.Message)

    async def PinMessageAsync(self, req:  models.PinMessageReq) ->  models.SimpleQueryResult:
        """
        Async version of PinMessage.

        Example:
            response = await api.chats.PinMessageAsync(PinMessageReq(
                chat_id=123456789,
                message_id="mid:987654321..."
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        return await adecode(self.client, "PUT", path,  models.SimpleQueryResult, payload=req)

    async def UnpinMessageAsync(self, req:  models.UnpinMessageReq) ->  models.SimpleQueryResult:
        """
        Async version of UnpinMessage.

        Example:
            response = await api.chats.UnpinMessageAsync(UnpinMessageReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        return await adecode(self.client, "DELETE", path,  models.SimpleQueryResult)

    async def GetChatMembershipAsync(self, req:  models.GetChatMembershipReq) ->  models.ChatMember:
        """
        Async version of GetChatMembership.

        Example:
            response = await api.chats.GetChatMembershipAsync(GetChatMembershipReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        return await adecode(self.client, "GET", path,  models.ChatMember)

    async def LeaveChatAsync(self, req:  models.LeaveChatReq) ->  models.SimpleQueryResult:
        """
        Async version of LeaveChat.

        Example:
            response = await api.chats.LeaveChatAsync(LeaveChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        return await adecode(self.client, "DELETE", path,  models.SimpleQueryResult)

    async def GetChatAdminsAsync(self, req:  models.GetChatAdminsReq) ->  models.GetChatAdminsResp:
        """
        Async version of GetChatAdmins.

        Example:
            response = await api.chats.GetChatAdminsAsync(GetChatAdminsReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        return await adecode(self.client, "GET", path,  models.GetChatAdminsResp)

    async def SetChatAdminsAsync(self, req:  models.SetChatAdminsReq) ->  models.SimpleQueryResult:
        """
        Async version of SetChatAdmins.

        Example:
            response = await api.chats.SetChatAdminsAsync(SetChatAdminsReq(
                chat_id=123456789,
                admins=[ChatAdmin(user_id=98765, role="admin")]
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        return await adecode(self.client, "POST", path,  models.SimpleQueryResult, payload=req)

    async def DeleteAdminAsync(self, req:  models.DeleteAdminReq) ->  models.SimpleQueryResult:
        """
        Async version of DeleteAdmin.

        Example:
            response = await api.chats.DeleteAdminAsync(DeleteAdminReq(
                chat_id=123456789,
                user_id=98765
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN_ID.format(req.chat_id, req.user_id)
        return await adecode(self.client, "DELETE", path,  models.SimpleQueryResult)

    async def GetChatMembersAsync(self, req:  models.GetChatMembersReq) ->  models.GetChatAdminsResp:
        """
        Async version of GetChatMembers.

        Example:
            response = await api.chats.GetChatMembersAsync(GetChatMembersReq(
                chat_id=123456789,
                count=20
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return await adecode(self.client, "GET", path,  models.GetChatAdminsResp, query=req.model_dump(exclude_none=True))

    async def AddMembersAsync(self, req:  models.AddMembersReq) ->  models.AddMembersResp:
        """
        Async version of AddMembers.

        Example:
            response = await api.chats.AddMembersAsync(AddMembersReq(
                chat_id=123456789,
                user_ids=[11111, 22222]
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return await adecode(self.client, "POST", path,  models.AddMembersResp, payload=req)

    async def DeleteMemberAsync(self, req:  models.DeleteMemberReq) ->  models.SimpleQueryResult:
        """
        Async version of DeleteMember.

        Example:
            response = await api.chats.DeleteMemberAsync(DeleteMemberReq(
                chat_id=123456789,
                user_id=98765
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        return await adecode(self.client, "DELETE", path, models.SimpleQueryResult, query=req.model_dump(exclude_none=True))