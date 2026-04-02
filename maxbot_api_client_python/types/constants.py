from enum import Enum

DEFAULT_BASE_URL = "https://platform-api.max.ru"

class Paths(str, Enum):
    ME = "me"
    CHATS = "chats"
    ANSWERS = "answers"
    UPDATES = "updates"
    UPLOADS = "uploads"
    MESSAGES = "messages"
    SUBSCRIPTIONS = "subscriptions"
    VIDEOS = "videos"

    CHATS_ID = "chats/{}"
    CHATS_PIN = "chats/{}/pin"
    CHATS_ACTIONS = "chats/{}/actions"
    CHATS_MEMBERS = "chats/{}/members"
    CHATS_MEMBERS_ME = "chats/{}/members/me"
    CHATS_MEMBERS_ADMIN = "chats/{}/members/admins"
    CHATS_MEMBERS_ADMIN_ID = "chats/{}/members/admins/{}"

class AttachmentType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"
    STICKER = "sticker"
    CONTACT = "contact"
    KEYBOARD = "inline_keyboard"
    SHARE = "share"
    LOCATION = "location"

class ChatType(str, Enum):
    CHANNEL = "channel"
    CHAT = "chat"
    DIALOG = "dialog"

class ChatStatus(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    LEFT = "left"
    REMOVED = "removed"

class MarkupType(str, Enum):
    STRONG = "strong"
    EMPHASIZED = "emphasized"
    MONOSPACED = "monospaced"
    LINK = "link"
    STRIKETHROUGH = "strikethrough"
    UNDERLINE = "underline"
    USER = "user_mention"

class Format(str, Enum):
    HTML = "html"
    MARKDOWN = "markdown"

class UpdateType(str, Enum):
    BOT_ADDED = "bot_added"
    BOT_REMOVED = "bot_removed"
    BOT_STARTED = "bot_started"
    BOT_STOPPED = "bot_stopped"
    CHAT_TITLE_CHANGED = "chat_title_changed"
    DIALOG_MUTED = "dialog_muted"
    DIALOG_UNMUTED = "dialog_unmuted"
    DIALOG_CLEARED = "dialog_cleared"
    DIALOG_REMOVED = "dialog_removed"
    MESSAGE_CREATED = "message_created"
    MESSAGE_CALLBACK = "message_callback"
    MESSAGE_EDITED = "message_edited"
    MESSAGE_REMOVED = "message_removed"
    USER_ADDED = "user_added"
    USER_REMOVED = "user_removed"

class LinkedMessageType(str, Enum):
    FORWARD = "forward"
    REPLY = "reply"

class SenderAction(str, Enum):
    TYPING_ON = "typing_on"
    TYPING_OFF = "typing_off"
    SENDING_PHOTO = "sending_photo"
    SENDING_VIDEO = "sending_video"
    SENDING_AUDIO = "sending_audio"
    SENDING_FILE = "sending_file"
    MARK_SEEN = "mark_seen"

class ChatAdminPermission(str, Enum):
    READ_ALL_MESSAGES = "read_all_messages"
    ADD_REMOVE_USERS = "add_remove_members"
    ADD_ADMINS = "add_admins"
    CHANGE_CHAT_PHOTO = "change_chat_info"
    PIN_MESSAGE = "pin_message"
    WRITE = "write"
    EDIT_LINK = "edit_link"

class ButtonType(str, Enum):
    CALLBACK = "callback"
    LINK = "link"
    REQUEST_LOCATION = "request_geo_location"
    REQUEST_CONTACT = "request_contact"
    OPEN_APP = "open_app"
    MESSAGE = "message"

class UploadType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"