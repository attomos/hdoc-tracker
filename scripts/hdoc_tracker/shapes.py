from typing import Any, Literal, TypedDict


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


class Entity(TypedDict):
    start: int
    end: int


class Hashtag(Entity):
    tag: str


class StatusUrl(Entity):
    url: str
    expanded_url: str
    display_url: str


class HdocDay(Entity):
    day: str


class Src(Entity):
    src: str
    fixed: bool


class Demo(Entity):
    demo: str
    fixed: bool


class Entities(TypedDict, total=False):
    hashtags: list[Hashtag]
    urls: list[StatusUrl]
    day_list: list[HdocDay]
    src_list: list[Src]
    demo_list: list[Demo]
