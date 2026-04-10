from typing import Any

from maxbot_api_client_python.client import Client
from maxbot_api_client_python.types.constants import Paths
from maxbot_api_client_python.types.models import (
    AddMembersReq, AddMembersResp, ChatInfo, ChatMember, DeleteAdminReq, DeleteChatReq, 
    DeleteMemberReq, EditChatReq, GetChatAdminsReq, GetChatAdminsResp, GetChatMembersReq, 
    GetChatMembersResp, GetChatMembershipReq, GetChatReq, GetChatsReq, GetChatsResp, 
    GetPinnedMessageReq, LeaveChatReq, Message, PinMessageReq, SendActionReq, 
    SetChatAdminsReq, SimpleQueryResult, UnpinMessageReq, ChatAdmin
)

class Chats:
    def __init__(self, client: Client):
        self.client = client

    def get_chats(self, req: GetChatsReq) -> GetChatsResp:
        """
        Returns information about chats that the bot participated in: a result list and a marker pointing to the next page.

        Example:
            response = bot.chats.get_chats(GetChatsReq(
                count=20
            ))
        """
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", Paths.CHATS, GetChatsResp, query=query, payload=payload)

    def get_chat(self, req: GetChatReq) -> ChatInfo:
        """
        Returns info about a specific chat.

        Example:
            response = bot.chats.get_chat(GetChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", path, ChatInfo, query=query, payload=payload)

    def edit_chat(self, req: EditChatReq) -> ChatInfo:
        """
        Modifies the properties of a chat, such as its title, icon, or notification settings.

        Example:
            response = bot.chats.edit_chat(EditChatReq(
                chat_id=123456789,
                title="Updated Chat Title",
                notify=True
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("PATCH", path, ChatInfo, query=query, payload=payload)

    def delete_chat(self, req: DeleteChatReq) -> SimpleQueryResult:
        """
        Permanently deletes a chat for the bot.

        Example:
            response = bot.chats.delete_chat(DeleteChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("DELETE", path, SimpleQueryResult, query=query, payload=payload)

    def send_action(self, req: SendActionReq) -> SimpleQueryResult:
        """
        Broadcasts a temporary status action (e.g., "typing...", "recording video...") to the chat participants.

        Example:
            response = bot.chats.send_action(SendActionReq(
                chat_id=123456789,
                action="mark_seen"
            ))
        """
        path = Paths.CHATS_ACTIONS.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("POST", path, SimpleQueryResult, query=query, payload=payload)

    def get_pinned_message(self, req: GetPinnedMessageReq) -> Message:
        """
        Retrieves the currently pinned message in the specified chat.

        Example:
            response = bot.chats.get_pinned_message(GetPinnedMessageReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", path, Message, query=query, payload=payload)

    def pin_message(self, req: PinMessageReq) -> SimpleQueryResult:
        """
        Pins a specific message in the chat.
        You can optionally specify whether to notify chat members about the new pinned message.

        Example:
            response = bot.chats.pin_message(PinMessageReq(
                chat_id=123456789,
                message_id="mid:987654321...",
                notify=True
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("PUT", path, SimpleQueryResult, query=query, payload=payload)

    def unpin_message(self, req: UnpinMessageReq) -> SimpleQueryResult:
        """
        Removes the pinned message from the specified chat.

        Example:
            response = bot.chats.unpin_message(UnpinMessageReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("DELETE", path, SimpleQueryResult, query=query, payload=payload)

    def get_chat_membership(self, req: GetChatMembershipReq) -> ChatMember:
        """
        Returns chat membership info for the current bot.

        Example:
            response = bot.chats.get_chat_membership(GetChatMembershipReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", path, ChatMember, query=query, payload=payload)

    def leave_chat(self, req: LeaveChatReq) -> SimpleQueryResult:
        """
        Removes the bot from chat members.

        Example:
            response = bot.chats.leave_chat(LeaveChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("DELETE", path, SimpleQueryResult, query=query, payload=payload)

    def get_chat_admins(self, req: GetChatAdminsReq) -> GetChatAdminsResp:
        """
        Retrieves a list of administrators for the specified group chat.

        Example:
            response = bot.chats.get_chat_admins(GetChatAdminsReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", path, GetChatAdminsResp, query=query, payload=payload)

    def set_chat_admins(self, req: SetChatAdminsReq) -> SimpleQueryResult:
        """
        Assigns administrator rights to specific users in a group chat.

        Example:
            response = bot.chats.set_chat_admins(SetChatAdminsReq(
                chat_id=123456789,
                admins=[
                    ChatAdmin(user_id=98765, role="admin"),
                    ChatAdmin(user_id=43210, role="admin")
                ]
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("POST", path, SimpleQueryResult, query=query, payload=payload)

    def delete_admin(self, req: DeleteAdminReq) -> SimpleQueryResult:
        """
        Revokes administrator rights from a specific user in a group chat.

        Example:
            response = bot.chats.delete_admin(DeleteAdminReq(
                chat_id=123456789,
                user_id=98765
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN_ID.format(req.chat_id, req.user_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("DELETE", path, SimpleQueryResult, query=query, payload=payload)

    def get_chat_members(self, req: GetChatMembersReq) -> GetChatMembersResp:
        """
        Returns users participated in the chat.

        Example:
            response = bot.chats.get_chat_members(GetChatMembersReq(
                chat_id=123456789,
                count=20
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("GET", path, GetChatMembersResp, query=query, payload=payload)

    def add_members(self, req: AddMembersReq) -> AddMembersResp:
        """
        Adds one or more users to a group chat.

        Example:
            response = bot.chats.add_members(AddMembersReq(
                chat_id=123456789,
                user_ids=[11111, 22222]
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("POST", path, AddMembersResp, query=query, payload=payload)

    def delete_member(self, req: DeleteMemberReq) -> SimpleQueryResult:
        """
        Removes a specific user from a group chat.
        You can optionally block the user from rejoining.

        Example:
            response = bot.chats.delete_member(DeleteMemberReq(
                chat_id=123456789,
                user_id=98765,
                block=True
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return self.client.decode("DELETE", path, SimpleQueryResult, query=query, payload=payload)

    async def get_chats_async(self, req: GetChatsReq) -> GetChatsResp:
        """
        Async version of get_chats.

        Example:
            response = await bot.chats.get_chats_async(GetChatsReq(
                count=20
            ))
        """
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", Paths.CHATS, GetChatsResp, query=query, payload=payload)

    async def get_chat_async(self, req: GetChatReq) -> ChatInfo:
        """
        Async version of get_chat.

        Example:
            response = await bot.chats.get_chat_async(GetChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", path, ChatInfo, query=query, payload=payload)
    
    async def edit_chat_async(self, req: EditChatReq) -> ChatInfo:
        """
        Async version of EditChat.

        Example:
            response = await bot.chats.edit_chat_async(EditChatReq(
                chat_id=123456789,
                title="Updated Chat Title"
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("PATCH", path, ChatInfo, query=query, payload=payload)

    async def delete_chat_async(self, req: DeleteChatReq) -> SimpleQueryResult:
        """
        Async version of DeleteChat.

        Example:
            response = await bot.chats.delete_chat_async(DeleteChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_ID.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("DELETE", path, SimpleQueryResult, query=query, payload=payload)

    async def send_action_async(self, req: SendActionReq) -> SimpleQueryResult:
        """
        Async version of SendAction.

        Example:
            response = await bot.chats.send_action_async(SendActionReq(
                chat_id=123456789,
                action="typing"
            ))
        """
        path = Paths.CHATS_ACTIONS.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("POST", path, SimpleQueryResult, query=query, payload=payload)

    async def get_pinned_message_async(self, req: GetPinnedMessageReq) -> Message:
        """
        Async version of GetPinnedMessage.

        Example:
            response = await bot.chats.get_pinned_message_async(GetPinnedMessageReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", path, Message, query=query, payload=payload)

    async def pin_message_async(self, req: PinMessageReq) -> SimpleQueryResult:
        """
        Async version of PinMessage.

        Example:
            response = await bot.chats.pin_message_async(PinMessageReq(
                chat_id=123456789,
                message_id="mid:987654321..."
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("PUT", path, SimpleQueryResult, query=query, payload=payload)

    async def unpin_message_async(self, req: UnpinMessageReq) -> SimpleQueryResult:
        """
        Async version of UnpinMessage.

        Example:
            response = await bot.chats.unpin_message_async(UnpinMessageReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_PIN.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("DELETE", path, SimpleQueryResult, query=query, payload=payload)

    async def get_chat_membership_async(self, req: GetChatMembershipReq) -> ChatMember:
        """
        Async version of GetChatMembership.

        Example:
            response = await bot.chats.get_chat_membership_async(GetChatMembershipReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", path, ChatMember, query=query, payload=payload)

    async def leave_chat_async(self, req: LeaveChatReq) -> SimpleQueryResult:
        """
        Async version of LeaveChat.

        Example:
            response = await bot.chats.leave_chat_async(LeaveChatReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ME.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("DELETE", path, SimpleQueryResult, query=query, payload=payload)

    async def get_chat_admins_async(self, req: GetChatAdminsReq) -> GetChatAdminsResp:
        """
        Async version of get_chatAdmins.

        Example:
            response = await bot.chats.get_chat_admins_async(GetChatAdminsReq(
                chat_id=123456789
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", path, GetChatAdminsResp, query=query, payload=payload)

    async def set_chat_admins_async(self, req: SetChatAdminsReq) -> SimpleQueryResult:
        """
        Async version of SetChatAdmins.

        Example:
            response = await bot.chats.set_chat_admins_async(SetChatAdminsReq(
                chat_id=123456789,
                admins=[ChatAdmin(user_id=98765, permissions=["admin"])]
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("POST", path, SimpleQueryResult, query=query, payload=payload)

    async def delete_admin_async(self, req: DeleteAdminReq) -> SimpleQueryResult:
        """
        Async version of DeleteAdmin.

        Example:
            response = await bot.chats.delete_admin_async(DeleteAdminReq(
                chat_id=123456789,
                user_id=98765
            ))
        """
        path = Paths.CHATS_MEMBERS_ADMIN_ID.format(req.chat_id, req.user_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("DELETE", path, SimpleQueryResult, query=query, payload=payload)

    async def get_chat_members_async(self, req: GetChatMembersReq) -> GetChatMembersResp:
        """
        Async version of GetChatMembers.

        Example:
            response = await bot.chats.get_chat_members_async(GetChatMembersReq(
                chat_id=123456789,
                count=20
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("GET", path, GetChatMembersResp, query=query, payload=payload)

    async def add_members_async(self, req: AddMembersReq) -> AddMembersResp:
        """
        Async version of AddMembers.

        Example:
            response = await bot.chats.add_members_async(AddMembersReq(
                chat_id=123456789,
                user_ids=[11111, 22222]
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("POST", path, AddMembersResp, query=query, payload=payload)

    async def delete_member_async(self, req: DeleteMemberReq) -> SimpleQueryResult:
        """
        Async version of DeleteMember.

        Example:
            response = await bot.chats.delete_member_async(DeleteMemberReq(
                chat_id=123456789,
                user_id=98765
            ))
        """
        path = Paths.CHATS_MEMBERS.format(req.chat_id)
        query, payload = self.client.split_request(req)
        return await self.client.adecode("DELETE", path, SimpleQueryResult, query=query, payload=payload)