from hdoc_tracker.shapes import Status, Tweet


def convert(tweet: Tweet) -> Status:
    return {
        "id": tweet["id"],
        "created_at": tweet["created_at"],
        "in_reply_to_id": tweet["conversation_id"],
        "url": f"https://twitter.com/attomos/status/{tweet['id']}",
        "content": tweet["text"],
        "parsed_content": tweet["text"],
        "media_attachments": [],
        "entities": tweet["entities"],
    }
