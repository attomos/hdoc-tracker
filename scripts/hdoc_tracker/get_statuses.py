import json
from pathlib import Path

import requests
import requests.utils
from bs4 import BeautifulSoup
from tinydb import Query, TinyDB

from hdoc_tracker.patterns import (
    DEMO_PATTERN,
    HDOC_PATTERN,
    MODERN_HDOC_PATTERN,
    MODERN_HDOC_PATTERN2,
    SRC_PATTERN,
)
from hdoc_tracker.shapes import Status
from hdoc_tracker.utils import get_extra_entities, parse_html_content

# TODO
# 1. Fetch statuses from the API using since_id and tagged params
# 2. Group statuses by in_reply_to_id (aka conversation_id in Twitter)
# 3. Create a simplified data format (the source will be only Mastodon from now on).
# 4. Upload the statuses file and stats file to Upstash OR find a better way.

SCRIPTS_DIR = Path(__file__).parent.parent


def fetch_statuses():
    results = []
    print("fetching statuses from Mastodon API...")
    response = requests.get(
        "https://mastodon.social/api/v1/accounts/110597468247904411/statuses?since_id=110597481161337224"
    )
    links = response.links
    results += response.json()
    while "next" in links:
        print("fetching next page...")
        response = requests.get(links["next"]["url"])
        links = response.links
        results += response.json()

    return results


def main():
    raw_statuses = fetch_statuses()
    statuses = []

    # refine each status object and enrich with entities
    for raw_status in raw_statuses:
        # exclude reblogs and non-#100DaysOfCode statuses
        tags_names = [tag["name"].lower() for tag in raw_status["tags"]]
        if raw_status.get("reblog") or (
            not raw_status["in_reply_to_id"] and "100daysofcode" not in tags_names
        ):
            print(f"skipping status {raw_status['id']}")
            continue
        status: Status = {
            "id": raw_status["id"],
            "created_at": raw_status["created_at"],
            "in_reply_to_id": raw_status["in_reply_to_id"],
            "url": raw_status["url"],
            "content": raw_status["content"],
            "parsed_content": parse_html_content(raw_status["content"]),
            "media_attachments": raw_status["media_attachments"],
            "entities": {},
        }
        text = status["parsed_content"]
        modern_hdoc_day = get_extra_entities(MODERN_HDOC_PATTERN, text)
        modern_hdoc_day2 = get_extra_entities(MODERN_HDOC_PATTERN2, text)
        hdoc_day = get_extra_entities(HDOC_PATTERN, text)
        src = get_extra_entities(SRC_PATTERN, text)
        demo = get_extra_entities(DEMO_PATTERN, text)
        entities = status["entities"]
        if modern_hdoc_day:
            entities.update(modern_hdoc_day)
        if modern_hdoc_day2:
            entities.update(modern_hdoc_day2)
        if hdoc_day:
            entities.update(hdoc_day)
        if src:
            entities.update(src)
        if demo:
            entities.update(demo)
        status["entities"] = entities
        statuses.append(status)

    # group status by in_reply_to_id (aka conversation_id in Twitter)
    grouped = {}
    for raw_status in statuses:
        key = raw_status["in_reply_to_id"] or raw_status["id"]
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(raw_status)

    (SCRIPTS_DIR / "round2.json").write_text(json.dumps(grouped, indent=2))
    for id, statuses in grouped.items():
        print(id, len(statuses))

    for raw_status in raw_statuses[:1]:
        print(raw_status["content"])
        print("")
        print("")


def main2():
    db = TinyDB("./stats.json")
    Stat = Query()
    db.insert(
        {
            "round": 1,
            "item_count": 1,
            "conversation_count": 1,
            "since_id": "1",
        }
    )
    db.update(
        {
            "item_count": 2,
            "conversation_count": 2,
            "since_id": "2",
        },
        Stat.round == 1,
    )
    # db.insert({"round": 1, "int": 1, "char": "a"})
    print(db.all())
    print("test")


if __name__ == "__main__":
    main()
    # main2()
