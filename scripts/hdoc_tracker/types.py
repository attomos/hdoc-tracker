from typing import Literal, TypedDict


class MediaAttachment(TypedDict):
    _type: Literal["image", "something"]
    url: str
    preview_url: str
    description: str
    blurhash: str


class Status(TypedDict):
    id: str
    created_at: str
    in_reply_to_id: str
    url: str
    content: str
    parsed_content: str
    media_attachments: list[MediaAttachment]
