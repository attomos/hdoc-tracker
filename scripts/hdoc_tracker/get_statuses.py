import json
from pathlib import Path

# TODO
# 1. Fetch statuses from the API using since_id and tagged params
# 2. Group statuses by in_reply_to_id (aka conversation_id in Twitter)
# 3. Transform statuses into hdoc format (GroupedTweets and Tweet).
#    Need to rename these types too.
# 4. Upload the statuses file and stats file to Upstash


def main():
    print("reading from mastodon.json")
    print("")

    # temporary, will read from the API later
    tt = (Path(__file__).parent / "mastodon.json").read_text()
    dd = json.loads(tt)

    # group status by in_reply_to_id (aka conversation_id in Twitter)
    grouped = {}
    for status in dd:
        key = status["in_reply_to_id"] or status["id"]
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(status)

    print(grouped)
    for id, statuses in grouped.items():
        print(id, len(statuses))
    for status in dd[:1]:
        print(status["content"])
        print("")
        print("")


if __name__ == "__main__":
    main()
