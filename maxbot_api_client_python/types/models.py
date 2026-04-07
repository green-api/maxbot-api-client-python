from __future__ import annotations
from typing import Any
from pydantic import BaseModel, Field, ConfigDict
from maxbot_api_client_python.types.constants import (
    AttachmentType, ChatType, ChatStatus, MarkupType, Format, UpdateType,
    LinkedMessageType, SenderAction, ChatAdminPermission, ButtonType, UploadType
)

class MaxBotModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)

class APIError(MaxBotModel):
    code: str
    message: str

class SimpleQueryResult(MaxBotModel):
    success: bool = Field(..., alias="success")
    message: str | None = Field(None, alias="message")


class User(MaxBotModel):
    user_id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None
    is_bot: bool
    last_activity_time: int

class BotCommand(MaxBotModel):
    name: str
    description: str | None = None

class BotInfo(User):
    description: str | None = None
    avatar_url: str | None = None
    full_avatar_url: str | None = None
    commands: list[BotCommand] | None = None

class DialogWithUser(User):
    description: str | None = None
    avatar_url: str
    full_avatar_url: str

class ChatMember(DialogWithUser):
    last_access_time: int
    is_owner: bool
    is_admin: bool
    join_time: int
    permissions: list[ChatAdminPermission]
    alias: str | None = None

class ChatAdmin(MaxBotModel):
    user_id: int
    permissions: list[ChatAdminPermission]
    alias: str | None = None

class Recipient(MaxBotModel):
    chat_id: int | None = None
    chat_type: ChatType
    user_id: int | None = None


class Image(MaxBotModel):
    url: str

class Photos(MaxBotModel):
    token: str

class PhotoData(MaxBotModel):
    token: str

class ImagePayload(MaxBotModel):
    photos: dict[str, PhotoData]

class StickerData(MaxBotModel):
    url: str | None = None
    code: str | None = None


class MediaPayload(MaxBotModel):
    url: str | None = None
    token: str | None = None

class PhotoAttachmentPayload(MaxBotModel):
    photo_id: int | None = None
    token: str | None = None
    url: str | None = None

class PhotoAttachmentRequestPayload(MaxBotModel):
    url: str
    token: str | None = None
    photos: dict[str, PhotoData] | None = None

class VideoAttachmentPayload(MediaPayload):
    thumbnail: str | None = None
    width: int | None = None
    height: int | None = None
    duration: int | None = None

class AudioAttachmentPayload(MediaPayload):
    transcription: str | None = None

class FileAttachmentPayload(MediaPayload):
    filename: str | None = None
    size: int | None = None

class StickerAttachmentPayload(StickerData):
    width: int | None = None
    height: int | None = None

class ContactAttachmentPayload(MaxBotModel):
    name: str | None = None
    contact_id: int | None = None
    vcf_info: str | None = None
    vcf_phone: str | None = None

class KeyboardButton(MaxBotModel):
    type: ButtonType
    text: str
    payload: str | None = None
    url: str | None = None
    quick: bool | None = None
    web_app: str | None = None
    contact_id: int | None = None

class Keyboard(MaxBotModel):
    buttons: list[list[KeyboardButton]]

class ShareAttachmentPayload(MaxBotModel):
    url: str | None = None
    token: str | None = None
    title: str | None = None
    description: str | None = None
    image_url: str | None = None

class AttachmentRequest(MaxBotModel):
    type: AttachmentType

class Attachment(MaxBotModel):
    type: AttachmentType
    payload: Any | None = None
    latitude: float | None = None
    longitude: float | None = None


class BotPatch(MaxBotModel):
    name: str | None = None
    username: str | None = None
    description: str | None = None
    commands: list[BotCommand] | None = None
    photo: PhotoAttachmentRequestPayload | None = None


class MarkupElement(MaxBotModel):
    type: MarkupType
    from_: int = Field(alias="from")
    length: int

class NewMessageLink(MaxBotModel):
    type: LinkedMessageType
    mid: str

class LinkedMessage(MaxBotModel):
    type: LinkedMessageType
    sender: User | None = None
    chat_id: int | None = None
    message: MessageBody | None = None

class MessageBody(MaxBotModel):
    mid: str
    seq: int
    text: str | None = None
    attachments: list[Attachment] | None = None
    markup: list[MarkupElement] | None = None

class NewMessageBody(MaxBotModel):
    text: str | None = None
    attachments: list[Attachment] | None = None
    link: NewMessageLink | None = None
    notify: bool | None = None
    format: Format | None = None

class MessageStat(MaxBotModel):
    views: int

class Message(MaxBotModel):
    sender: User | None = None
    recipient: Recipient | None = None
    timestamp: int | None = None
    linked_message: LinkedMessage | None = Field(None, alias="link")
    body: MessageBody | None = None
    stat: MessageStat | None = None
    url: str | None = None

class MessagesList(MaxBotModel):
    messages: list[Message]


class Chat(MaxBotModel):
    chat_id: int
    type: ChatType
    status: ChatStatus
    title: str | None = None
    icon: Image | None = None
    last_event_time: int
    participants_count: int | None = None
    owner_id: int | None = None
    participants: dict[str, int] | None = None
    is_public: bool
    link: str | None = None
    description: str | None = None
    dialog_with_user: DialogWithUser | None = None
    chat_message_id: str | None = None
    pinned_message: Message | None = None

class ChatInfo(MaxBotModel):
    chat_id: int
    type: ChatType
    status: ChatStatus
    title: str | None = None
    icon: Image | None = None
    last_event_time: int
    participants_count: int | None = None
    owner_id: int | None = None
    participants: dict[str, int] | None = None
    is_public: bool
    link: str | None = None
    description: str | None = None
    dialog_with_user: list[DialogWithUser] | None = None
    chat_message_id: str | None = None
    pinned_message: list[Message] | None = None


class Callback(MaxBotModel):
    timestamp: int
    callback_id: str
    payload: str | None = None
    user: User

class Update(MaxBotModel):
    update_type: UpdateType
    timestamp: int
    callback: Callback | None = None
    message: Message | None = None
    message_id: str | None = None
    chat_id: int | None = None
    user_id: int | None = None
    muted_until: int | None = None
    user_locale: str | None = None
    is_channel: bool | None = None

class MessageCallbackUpdate(Update):
    callback: Callback
    message: Message | None = None

class Subscription(MaxBotModel):
    url: str
    time: int
    update_types: list[UpdateType] | None = None


class GetChatsReq(MaxBotModel):
    count: int | None = Field(None, alias="count")
    marker: int | None = Field(None, alias="marker")

class GetChatsResp(MaxBotModel):
    chats: list[Chat]
    marker: int | None = None

class GetChatReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")

class EditChatReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    icon: Image | None = None
    title: str | None = None
    pin: str | None = None
    notify: bool | None = None

class DeleteChatReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")

class SendActionReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    action: SenderAction

class PinMessageReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    message_id: str
    notify: bool | None = None

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
    members: list[ChatMember]
    marker: int | None = None

class SetChatAdminsReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    admins: list[ChatAdmin]
    marker: int | None = None

class DeleteAdminReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    user_id: int = Field(..., alias="userId")

class GetChatMembersReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    user_ids: list[int] | None = Field(None, alias="user_ids")
    marker: int | None = Field(None, alias="marker")
    count: int | None = Field(None, alias="count")

class AddMembersReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    user_ids: list[int] | None = None

class FailedUserDetails(MaxBotModel):
    error_code: str
    user_ids: list[int]

class AddMembersResp(SimpleQueryResult):
    failed_user_ids: list[int] | None = Field(None, alias="failed_user_ids")
    failed_user_details: list[FailedUserDetails] | None = Field(None, alias="failed_user_details")

class DeleteMemberReq(MaxBotModel):
    chat_id: int = Field(..., alias="chatId")
    user_id: int = Field(..., alias="userId")
    block: bool | None = Field(None, alias="block")


class GetMessagesReq(MaxBotModel):
    chat_id: int | None = Field(None, alias="chat_id")
    message_ids: list[str] | None = Field(None, alias="message_ids")
    from_: int | None = Field(None, alias="from")
    to: int | None = Field(None, alias="to")
    count: int | None = Field(None, alias="count")

class SendMessageReq(MaxBotModel):
    user_id: int | None = Field(None, alias="user_id")
    chat_id: int | None = Field(None, alias="chat_id")
    text: str | None = None
    format: Format | None = None
    notify: bool | None = None
    attachments: list[Attachment] | None = None
    link: NewMessageLink | None = None
    disable_link_preview: bool | None = Field(None, alias="disable_link_preview")

class SendMessageResp(MaxBotModel):
    message: Message

class EditMessageReq(MaxBotModel):
    message_id: str = Field(..., alias="message_id")
    text: str | None = None
    attachments: list[Attachment] | None = None
    link: NewMessageLink | None = None
    notify: bool | None = None
    format: Format | None = None

class DeleteMessageReq(MaxBotModel):
    message_id: str = Field(..., alias="message_id")

class GetMessageReq(MaxBotModel):
    message_id: str = Field(..., alias="message_id")

class VideoUrls(MaxBotModel):
    mp4_1080: str | None = None
    mp4_720: str | None = None
    mp4_480: str | None = None
    mp4_360: str | None = None
    mp4_240: str | None = None
    mp4_144: str | None = None
    hls: str | None = None

class VideoInfo(MaxBotModel):
    id: str
    status: str
    duration: int
    url: str

class GetVideoInfoReq(MaxBotModel):
    video_token: str = Field(..., alias="video_token")

class GetVideoInfoResp(MaxBotModel):
    token: str
    urls: VideoUrls | None = None
    thumbnail: PhotoAttachmentPayload | None = None
    width: int | None = None
    height: int | None = None
    duration: int | None = None

class AnswerCallbackReq(MaxBotModel):
    callback_id: str = Field(..., alias="callback_id")
    message: NewMessageBody | None = None
    notification: str | None = None

class SendFileReq(MaxBotModel):
    user_id: int | None = Field(None, alias="user_id")
    chat_id: int | None = Field(None, alias="chat_id")
    text: str | None = None
    format: Format | None = None
    notify: bool | None = None
    file_source: str
    link: NewMessageLink | None = None
    disable_link_preview: bool | None = Field(None, alias="disable_link_preview")
    attachments: list[Attachment] | None = None


class GetSubscriptionsResp(MaxBotModel):
    subscriptions: list[Subscription]

class SubscribeReq(MaxBotModel):
    url: str
    update_types: list[UpdateType] | None = None
    secret: str | None = None

class UnsubscribeReq(MaxBotModel):
    url: str = Field(..., alias="url")

class GetUpdatesReq(MaxBotModel):
    limit: int | None = Field(None, alias="limit")
    timeout: int | None = Field(None, alias="timeout")
    marker: int | None = Field(None, alias="marker")
    types: list[UpdateType] | None = Field(None, alias="types")

class GetUpdatesResp(MaxBotModel):
    updates: list[Update]
    marker: int


class UploadFileReq(MaxBotModel):
    type: UploadType = Field(..., alias="type")
    upload_url: str | None = None
    file_path: str | None = None

class UploadTypeReq(MaxBotModel):
    type: UploadType = Field(..., alias="type")

class UploadFileMultipartReq(MaxBotModel):
    upload_url: str
    file_path: str

class UploadedInfo(MaxBotModel):
    file_id: int | None = None
    token: str | None = None
    photos: dict[str, PhotoData] | None = None