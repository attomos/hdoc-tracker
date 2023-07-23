from typing import Any, Literal, NotRequired, TypedDict


class MediaAttachment(TypedDict):
    _type: Literal["image", "something"]
    url: str
    preview_url: str
    description: str
    blurhash: str


class Status(TypedDict):
    id: str
    created_at: str
    in_reply_to_id: str | None
    url: str
    content: str
    parsed_content: str
    media_attachments: list[MediaAttachment]
    entities: Any  # TODO make this a real type


class Tweet(TypedDict):
    id: str
    created_at: str
    conversation_id: str
    entities: Any  # TODO
    text: str


class LegacyTweets(TypedDict):
    data: list[Tweet]
