from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from .constants import (
    AttachmentType, ChatType, ChatStatus, MarkupType, Format, UpdateType,
    LinkedMessageType, SenderAction, ChatAdminPermission, ButtonType, UploadType
)

class MaxBotModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)

class APIError(MaxBotModel):
    code: str
    message: str

class Attachment(MaxBotModel):
    type: AttachmentType
    payload: Optional[Any] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class ImagePayload(MaxBotModel):
    photos: Dict[str, PhotoData]

class PhotoData(MaxBotModel):
    token: str

class AttachmentRequest(MaxBotModel):
    type: AttachmentType

class PhotoAttachmentPayload(MaxBotModel):
    photo_id: Optional[int] = None
    token: Optional[str] = None
    url: Optional[str] = None

class MediaPayload(MaxBotModel):
    url: Optional[str] = None
    token: Optional[str] = None

class VideoAttachmentPayload(MediaPayload):
    thumbnail: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None

class AudioAttachmentPayload(MediaPayload):
    transcription: Optional[str] = None

class FileAttachmentPayload(MediaPayload):
    filename: Optional[str] = None
    size: Optional[int] = None

class StickerData(MaxBotModel):
    url: Optional[str] = None
    code: Optional[str] = None

class StickerAttachmentPayload(StickerData):
    width: Optional[int] = None
    height: Optional[int] = None

class ContactAttachmentPayload(MaxBotModel):
    name: Optional[str] = None
    contact_id: Optional[int] = None
    vcf_info: Optional[str] = None
    vcf_phone: Optional[str] = None

class KeyboardButton(MaxBotModel):
    type: ButtonType
    text: str
    payload: Optional[str] = None
    url: Optional[str] = None
    quick: Optional[bool] = None
    web_app: Optional[str] = None
    contact_id: Optional[int] = None

class Keyboard(MaxBotModel):
    buttons: List[List[KeyboardButton]]

class ShareAttachmentPayload(MaxBotModel):
    url: Optional[str] = None
    token: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None

class BotCommand(MaxBotModel):
    name: str
    description: Optional[str] = None

class User(MaxBotModel):
    user_id: int
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    is_bot: bool
    last_activity_time: int

class BotInfo(User):
    description: Optional[str] = None
    avatar_url: Optional[str] = None
    full_avatar_url: Optional[str] = None
    commands: Optional[List[BotCommand]] = None

class PhotoAttachmentRequestPayload(MaxBotModel):
    url: str
    token: Optional[str] = None
    photos: Optional[Dict[str, PhotoData]] = None

class BotPatch(MaxBotModel):
    name: Optional[str] = None
    username: Optional[str] = None
    description: Optional[str] = None
    commands: Optional[List[BotCommand]] = None
    photo: Optional[PhotoAttachmentRequestPayload] = None

class Image(MaxBotModel):
    url: str

class DialogWithUser(User):
    description: Optional[str] = None
    avatar_url: str
    full_avatar_url: str

class ChatMember(DialogWithUser):
    last_access_time: int
    is_owner: bool
    is_admin: bool
    join_time: int
    permissions: List[ChatAdminPermission]
    alias: Optional[str] = None

class ChatAdmin(MaxBotModel):
    user_id: int
    permissions: List[ChatAdminPermission]
    alias: Optional[str] = None

class Recipient(MaxBotModel):
    chat_id: Optional[int] = None
    chat_type: ChatType
    user_id: Optional[int] = None

class LinkedMessage(MaxBotModel):
    type: LinkedMessageType
    sender: Optional[User] = None
    chat_id: Optional[int] = None
    message: Optional[MessageBody] = None

class MarkupElement(MaxBotModel):
    type: MarkupType
    from_: int = Field(alias="from")
    length: int

class MessageBody(MaxBotModel):
    mid: str
    seq: int
    text: Optional[str] = None
    attachments: Optional[List[Attachment]] = None
    markup: Optional[List[MarkupElement]] = None

class MessageStat(MaxBotModel):
    views: int

class Message(MaxBotModel):
    sender: Optional[User] = None
    recipient: Optional[Recipient] = None
    timestamp: Optional[int] = None
    linked_message: Optional[LinkedMessage] = Field(None, alias="link")
    body: Optional[MessageBody] = None
    stat: Optional[MessageStat] = None
    url: Optional[str] = None

class MessagesList(MaxBotModel):
    messages: List[Message]
    
class Chat(MaxBotModel):
    chat_id: int
    type: ChatType
    status: ChatStatus
    title: Optional[str] = None
    icon: Optional[Image] = None
    last_event_time: int
    participants_count: int
    owner_id: Optional[int] = None
    participants: Optional[Dict[str, int]] = None
    is_public: bool
    link: Optional[str] = None
    description: Optional[str] = None
    dialog_with_user: Optional[DialogWithUser] = None
    chat_message_id: str
    pinned_message: Optional[Message] = None

class ChatInfo(MaxBotModel):
    chat_id: int
    type: ChatType
    status: ChatStatus
    title: Optional[str] = None
    icon: Optional[Image] = None
    last_event_time: int
    participants_count: Optional[int] = None
    owner_id: Optional[int] = None
    participants: Optional[Dict[str, int]] = None
    is_public: bool
    link: Optional[str] = None
    description: Optional[str] = None
    dialog_with_user: Optional[List[DialogWithUser]] = None
    chat_message_id: Optional[str] = None
    pinned_message: Optional[List[Message]] = None

class Photos(MaxBotModel):
    token: str

class VideoInfo(MaxBotModel):
    id: str
    status: str
    duration: int
    url: str

class VideoUrls(MaxBotModel):
    mp4_1080: Optional[str] = None
    mp4_720: Optional[str] = None
    mp4_480: Optional[str] = None
    mp4_360: Optional[str] = None
    mp4_240: Optional[str] = None
    mp4_144: Optional[str] = None
    hls: Optional[str] = None

class NewMessageLink(MaxBotModel):
    type: LinkedMessageType
    mid: str

class NewMessageBody(MaxBotModel):
    text: Optional[str] = None
    attachments: Optional[List[Attachment]] = None
    link: Optional[NewMessageLink] = None
    notify: Optional[bool] = None
    format: Optional[Format] = None

class Callback(MaxBotModel):
    timestamp: int
    callback_id: str
    payload: Optional[str] = None
    user: User

class Update(MaxBotModel):
    update_type: UpdateType
    timestamp: int
    callback: Optional[Callback] = None
    message: Message
    message_id: Optional[str] = None
    chat_id: Optional[int] = None
    user_id: Optional[int] = None
    muted_until: Optional[int] = None
    user_locale: Optional[str] = None
    is_channel: Optional[bool] = None

class Subscription(MaxBotModel):
    url: str
    time: int
    update_types: Optional[List[UpdateType]] = None

class MessageCallbackUpdate(Update):
    callback: Callback
    message: Optional[Message] = None

class FailedUserDetails(MaxBotModel):
    error_code: str
    user_ids: List[int]

class GetChatsReq(MaxBotModel):
    count: Optional[int] = Field(None, alias="count")
    marker: Optional[int] = Field(None, alias="marker")

class GetChatsResp(MaxBotModel):
    chats: List[Chat]
    marker: Optional[int] = None

class GetChatReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")

class EditChatReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    icon: Optional[Image] = None
    title: Optional[str] = None
    pin: Optional[str] = None
    notify: Optional[bool] = None

class DeleteChatReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")

class SendActionReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    action: SenderAction

class PinMessageReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    message_id: str
    notify: Optional[bool] = None

class UnpinMessageReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")

class GetPinnedMessageReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")

class GetChatMembershipReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")

class LeaveChatReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")

class GetChatAdminsReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")

class GetChatAdminsResp(MaxBotModel):
    members: List[ChatMember]
    marker: Optional[int] = None

class SetChatAdminsReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    admins: List[ChatAdmin]
    marker: Optional[int] = None

class DeleteAdminReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    user_id: int = Field(..., alias="userId")

class GetChatMembersReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    user_ids: Optional[List[int]] = Field(None, alias="user_ids")
    marker: Optional[int] = Field(None, alias="marker")
    count: Optional[int] = Field(None, alias="count")

class AddMembersReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    user_ids: Optional[List[int]] = None

class SimpleQueryResult(MaxBotModel):
    success: bool = Field(..., alias="success")
    message: Optional[str] = Field(None, alias="message")

class AddMembersResp(SimpleQueryResult):
    failed_user_ids: Optional[List[int]] = Field(None, alias="failed_user_ids")
    failed_user_details: Optional[List[FailedUserDetails]] = Field(None, alias="failed_user_details")

class DeleteMemberReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    user_id: int = Field(..., alias="userId")
    block: Optional[bool] = Field(None, alias="block")

class GetSubscriptionsResp(MaxBotModel):
    subscriptions: List[Subscription]

class SubscribeReq(MaxBotModel):
    url: str
    update_types: Optional[List[UpdateType]] = None
    secret: Optional[str] = None

class UnsubscribeReq(MaxBotModel):
    url: str = Field(..., alias="url")

class GetUpdatesReq(MaxBotModel):
    limit: Optional[int] = Field(None, alias="limit")
    timeout: Optional[int] = Field(None, alias="timeout")
    marker: Optional[int] = Field(None, alias="marker")
    types: Optional[List[UpdateType]] = Field(None, alias="types")

class GetUpdatesResp(MaxBotModel):
    updates: List[Update]
    marker: int

class UploadFileReq(MaxBotModel):
    type: UploadType = Field(..., alias="type")
    upload_url: Optional[str] = None
    file_path: Optional[str] = None

class UploadTypeReq(MaxBotModel):
    type: UploadType = Field(..., alias="type")

class UploadFileMultipartReq(MaxBotModel):
    upload_url: str
    file_path: str

class UploadedInfo(MaxBotModel):
    file_id: Optional[int] = None
    token: Optional[str] = None
    photos: Optional[Dict[str, PhotoData]] = None

class GetMessagesReq(MaxBotModel):
    chat_id: Optional[int] = Field(None, alias="chat_id")
    message_ids: Optional[List[str]] = Field(None, alias="message_ids")
    from_: Optional[int] = Field(None, alias="from")
    to: Optional[int] = Field(None, alias="to")
    count: Optional[int] = Field(None, alias="count")

class SendMessageReq(MaxBotModel):
    user_id: Optional[int] = Field(None, alias="user_id")
    chat_id: Optional[int] = Field(None, alias="chat_id")
    text: Optional[str] = None
    format: Optional[Format] = None
    notify: Optional[bool] = None
    attachments: Optional[List[Attachment]] = None
    link: Optional[NewMessageLink] = None
    disable_link_preview: Optional[bool] = Field(None, alias="disable_link_preview")

class SendMessageResp(MaxBotModel):
    message: Message

class EditMessageReq(MaxBotModel):
    message_id: str = Field(..., alias="message_id")
    text: Optional[str] = None
    attachments: Optional[List[Attachment]] = None
    link: Optional[NewMessageLink] = None
    notify: Optional[bool] = None
    format: Optional[Format] = None

class DeleteMessageReq(MaxBotModel):
    message_id: str = Field(..., alias="message_id")

class GetMessageReq(MaxBotModel):
    message_id: str = Field(..., alias="message_id")

class GetVideoInfoReq(MaxBotModel):
    video_token: str = Field(..., alias="video_token")

class GetVideoInfoResp(MaxBotModel):
    token: str
    urls: Optional[VideoUrls] = None
    thumbnail: Optional[PhotoAttachmentPayload] = None
    width: Optional[int] = None
    height: Optional[int] = None
    duration: Optional[int] = None

class AnswerCallbackReq(MaxBotModel):
    callback_id: str = Field(..., alias="callback_id")
    message: Optional[NewMessageBody] = None
    notification: Optional[str] = None

class SendFileReq(MaxBotModel):
    user_id: Optional[int] = Field(None, alias="user_id")
    chat_id: Optional[int] = Field(None, alias="chat_id")
    text: Optional[str] = None
    format: Optional[Format] = None
    notify: Optional[bool] = None
    file_source: str
    link: Optional[NewMessageLink] = None
    disable_link_preview: Optional[bool] = Field(None, alias="disable_link_preview")
    attachments: Optional[List[Attachment]] = None