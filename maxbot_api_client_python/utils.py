from __future__ import annotations

from maxbot_api_client_python.types.models import (
    Attachment, AttachmentType, AudioAttachmentPayload, ContactAttachmentPayload,
    FileAttachmentPayload, Keyboard, KeyboardButton, PhotoAttachmentPayload,
    ShareAttachmentPayload, StickerAttachmentPayload, VideoAttachmentPayload
)

def attach_image(token: str | None = None, url: str | None = None) -> Attachment:
    return Attachment(
        type=AttachmentType.IMAGE,
        payload=PhotoAttachmentPayload(token=token, url=url).model_dump(exclude_none=True)
    )

def attach_video(token: str | None = None, url: str | None = None) -> Attachment:
    return Attachment(
        type=AttachmentType.VIDEO,
        payload=VideoAttachmentPayload(token=token, url=url).model_dump(exclude_none=True)
    )

def attach_audio(token: str | None = None, url: str | None = None) -> Attachment:
    return Attachment(
        type=AttachmentType.AUDIO,
        payload=AudioAttachmentPayload(token=token, url=url).model_dump(exclude_none=True)
    )

def attach_file(token: str | None = None, url: str | None = None, filename: str | None = None) -> Attachment:
    return Attachment(
        type=AttachmentType.FILE,
        payload=FileAttachmentPayload(token=token, url=url, filename=filename).model_dump(exclude_none=True)
    )

def attach_sticker(url: str | None = None, code: str | None = None) -> Attachment:
    return Attachment(
        type=AttachmentType.STICKER,
        payload=StickerAttachmentPayload(url=url, code=code).model_dump(exclude_none=True)
    )

def attach_contact(name: str, phone: str, contact_id: int | None = None) -> Attachment:
    vcf_info = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEND:VCARD"
    return Attachment(
        type=AttachmentType.CONTACT,
        payload=ContactAttachmentPayload(
            name=name,
            contact_id=contact_id,
            vcf_info=vcf_info,
            vcf_phone=phone
        ).model_dump(exclude_none=True)
    )

def attach_keyboard(buttons: list[list[KeyboardButton]]) -> Attachment:
    return Attachment(
        type=AttachmentType.KEYBOARD,
        payload=Keyboard(buttons=buttons).model_dump(exclude_none=True)
    )

def attach_share(url: str | None = None, title: str | None = None, desc: str | None = None) -> Attachment:
    return Attachment(
        type=AttachmentType.SHARE,
        payload=ShareAttachmentPayload(url=url, title=title, description=desc).model_dump(exclude_none=True)
    )

def attach_location(lat: float, lon: float) -> Attachment:
    return Attachment(
        type=AttachmentType.LOCATION,
        latitude=lat,
        longitude=lon
    )