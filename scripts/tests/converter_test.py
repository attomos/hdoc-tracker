from hdoc_tracker.converter import convert
from hdoc_tracker.shapes import Tweet


def test_convert():
    tweet: Tweet = {
        "id": "123",
        "created_at": "2021-01-01",
        "conversation_id": "456",
        "entities": {},
        "text": "hello world",
    }
    mastodon_status = convert(tweet)
    assert mastodon_status == {
        "id": "123",
        "created_at": "2021-01-01",
        "in_reply_to_id": "456",
        "url": "https://twitter.com/attomos/status/123",
        "content": "hello world",
        "parsed_content": "hello world",
        "media_attachments": [],
        "entities": {},
    }
