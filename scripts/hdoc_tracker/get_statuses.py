import json
from pathlib import Path

from bs4 import BeautifulSoup
from tinydb import Query, TinyDB

from hdoc_tracker.shapes import Status

# TODO
# 1. Fetch statuses from the API using since_id and tagged params
# 2. Group statuses by in_reply_to_id (aka conversation_id in Twitter)
# 3. Create a simplified data format (the source will be only Mastodon from now on).
# 4. Upload the statuses file and stats file to Upstash OR find a better way.

SCRIPTS_DIR = Path(__file__).parent.parent


def main():
    print("reading from mastodon.json")
    print("")

    # temporary, will read from the API later
    tt = (SCRIPTS_DIR / "mastodon.json").read_text()
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
    for raw_status in statuses:
        key = raw_status["in_reply_to_id"] or raw_status["id"]
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(raw_status)

    (SCRIPTS_DIR / "grouped.json").write_text(json.dumps(grouped, indent=2))
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


def main3():
    parsed = (
        BeautifulSoup(
            """<p><a href=\"https://mastodon.social/tags/100DaysOfCode\" class=\"mention hashtag\" rel=\"tag\">#<span>100DaysOfCode</span></a> R2D18</p><p>Continue working on hdoc-tracker.</p><p>Read Mastodon API docs and source code to figure out the best way to create data collection job.</p><p>I&#39;m going to keep things simple for round 2 and the subsequent rounds.<br />As for data from round 1, I will transform everything to be closest to Mastodon format as much as possible and rename all Twitter/Tweet occurrences from the source code to Mastodon terms.</p>""",
            "html.parser",
        ).get_text(separator="\n"),
    )

    print(parsed)


if __name__ == "__main__":
    # main()
    # main2()
    main3()
