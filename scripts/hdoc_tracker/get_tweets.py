import json
import os
from pathlib import Path
from timeit import default_timer as timer
from typing import Dict, List, Tuple

import requests
from dotenv import load_dotenv
from prettytable import PrettyTable, MARKDOWN


from hdoc_tracker.utils import (
    add_extra_entities_to_tweets,
    get_recent_index,
    group_tweets_by_conversation_id,
    group_tweets_by_round,
    load_stats,
    merge_tweets,
    update_stats,
)

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN", "")

# my first round of #100DaysOfCode, probably YAGNI because since_id
# but cannot underestimate people with 300k++ tweets in case I want to support
# another user as well
DEFAULT_START_TIME = "2022-01-01T00:00:00Z"


def make_request(url, headers, payload, hashtags_filter: List[str] = []) -> Dict:
    hashtags_set = set(hashtags_filter)
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {"error": response.json}

    json_response = response.json()
    if hashtags_filter:
        data = json_response.get("data", [])
        filtered_tweets = []
        for tweet in data:
            tags = set(
                [ht.get("tag") for ht in tweet.get("entities", {}).get("hashtags", [])]
            )
            if tags.intersection(hashtags_set):
                filtered_tweets.append(tweet)
        return {
            "data": filtered_tweets,
            "meta": json_response.get("meta"),
        }
    return json_response


def get_tweets(previous_stats: Dict) -> Tuple[Dict, Dict]:
    stats = {"total_tweets_count": 0}
    total_tweets_count = 0

    payload = {
        "tweet.fields": "conversation_id,created_at,entities,public_metrics,author_id",
        "max_results": 100,
        "exclude": "retweets",
    }

    if "since_id" in previous_stats:
        payload["since_id"] = previous_stats["since_id"]

    if "start_time" in previous_stats:
        payload["start_time"] = previous_stats["start_time"]

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
    }

    ID = "2699175613"
    HASHTAGS_FILTER = ["100DaysOfCode"]
    url = f"https://api.twitter.com/2/users/{ID}/tweets"

    print(payload)
    print("making initial request...")
    response = make_request(url, headers, payload, HASHTAGS_FILTER)

    data: Dict[str, List] = {"data": []}
    data["data"] += response["data"]
    print(len(response["data"]))
    total_tweets_count += len(response["data"])
    next_token = response.get("meta", {}).get("next_token", "")
    while next_token:
        payload["pagination_token"] = next_token
        print(payload)
        print(f"making another request (pagination_token: {next_token})...")
        response = make_request(url, headers, payload, HASHTAGS_FILTER)
        data["data"] += response["data"]
        print(len(response["data"]))
        total_tweets_count += len(response["data"])
        next_token = response.get("meta", {}).get("next_token", "")

    stats["total_tweets_count"] = total_tweets_count
    return data, stats


def main():
    start = timer()
    previous_stats = {"start_time": DEFAULT_START_TIME, **load_stats()}
    tweets, new_stats = get_tweets(previous_stats)
    tweets = add_extra_entities_to_tweets(tweets)
    grouped_tweets = group_tweets_by_conversation_id(tweets)
    rounds = group_tweets_by_round(grouped_tweets)

    for round, conversation_ids in rounds.items():
        print(conversation_ids)
        updated_tweets = {
            k: v for k, v in grouped_tweets.items() if k in conversation_ids
        }
        path = Path(f"{round}.json")
        if path.exists():
            tweets_json = json.loads(path.read_text())
            merged_tweets = merge_tweets(tweets_json, updated_tweets)
        else:
            merged_tweets = updated_tweets
        new_stats[f"{round} conversation count"] = len(merged_tweets.keys())
        t0 = [tweets for _, tweets in merged_tweets.items()]
        flatten = [item for sublist in t0 for item in sublist]
        new_stats[f"{round} tweets count"] = len(flatten)
        path.write_text(json.dumps(merged_tweets))

    end = timer()
    new_stats["time_taken"] = end - start
    conversation_ids = sorted(
        [tweet.get("conversation_id") for tweet in tweets.get("data", [])]
    )
    recent_index = get_recent_index(conversation_ids)
    try:
        recent_conversation_id = conversation_ids[recent_index]
        new_stats["since_id"] = recent_conversation_id
    except IndexError as e:
        print(e)
        print("possibly up-to-date, no need to update since_id")
        new_stats["since_id"] = previous_stats["since_id"]
    pt = PrettyTable()
    pt.set_style(MARKDOWN)
    pt.field_names = ["field", "data"]
    if "since_id" in previous_stats:
        pt.add_row(["previous since_id", previous_stats["since_id"]])
    for k, v in new_stats.items():
        pt.add_row([k, v])
    print(pt)
    update_stats(json.dumps(new_stats))


if __name__ == "__main__":
    main()
