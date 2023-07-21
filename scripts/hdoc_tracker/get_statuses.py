import json
from pathlib import Path

from bs4 import BeautifulSoup

from hdoc_tracker.types import Status

# TODO
# 1. Fetch statuses from the API using since_id and tagged params
# 2. Group statuses by in_reply_to_id (aka conversation_id in Twitter)
# 3. Create a simplified data format (the source will be only Mastodon from now on).
# 4. Upload the statuses file and stats file to Upstash OR find a better way.

CURRENT_DIR = Path(__file__).parent


def main():
    print("reading from mastodon.json")
    print("")

    # temporary, will read from the API later
    tt = (CURRENT_DIR / "mastodon.json").read_text()
    raw_statuses = json.loads(tt)
    statuses = []

    for raw_status in raw_statuses:
        status: Status = {
            "id": raw_status["id"],
            "created_at": raw_status["created_at"],
            "in_reply_to_id": raw_status["in_reply_to_id"],
            "url": raw_status["url"],
            "content": raw_status["content"],
            "parsed_content": BeautifulSoup(
                raw_status["content"], "html.parser"
            ).get_text(separator="\n"),
            "media_attachments": raw_status["media_attachments"],
        }
        statuses.append(status)

    # group status by in_reply_to_id (aka conversation_id in Twitter)
    grouped = {}
    for raw_status in statuses[::-1]:
        key = raw_status["in_reply_to_id"] or raw_status["id"]
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(raw_status)

    (CURRENT_DIR / "grouped.json").write_text(json.dumps(grouped, indent=2))
    for id, statuses in grouped.items():
        print(id, len(statuses))

    for raw_status in raw_statuses[:1]:
        print(raw_status["content"])
        print("")
        print("")


if __name__ == "__main__":
    main()
