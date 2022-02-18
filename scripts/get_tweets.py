import json
import os
import re
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List
from typing import OrderedDict as OD

import requests
from dotenv import load_dotenv

load_dotenv()


PATTERN = r"(([Dd]ay \d{1,3}) of|R\d{1,2}D\d{1,3}) #100DaysOfCode"
BEARER_TOKEN = os.getenv("BEARER_TOKEN", "")

print(BEARER_TOKEN[:4])


def make_request(url, headers, payload, hashtags_filter: List[str] = []) -> Dict:
    hashtags_set = set(hashtags_filter)
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {"error": response.json}

    json_response = response.json()
    if hashtags_filter:
        data = json_response["data"]
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


def get_tweets() -> Dict:
    # TODO: use since_id
    # TODO: remove hard-coded start_time
    # TODO: setup GitHub Actions to automatically update tweets
    payload = {
        "tweet.fields": "conversation_id,created_at,entities,public_metrics",
        "max_results": 100,
        "exclude": "retweets",
        "start_time": "2022-01-01T00:00:00Z",
    }

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
    next_token = response.get("meta", {}).get("next_token", "")
    while next_token:
        payload["pagination_token"] = next_token
        print(payload)
        print(f"making another request (pagination_token: {next_token})...")
        response = make_request(url, headers, payload, HASHTAGS_FILTER)
        data["data"] += response["data"]
        print(len(response["data"]))
        next_token = response.get("meta", {}).get("next_token", "")

    return data


def get_hdoc_day(pattern, text):
    if m := re.match(pattern, text):
        if len(m.groups()) == 2:
            hdoc_day = m.group(2)
            start, end = m.span(2)
            return {"days": [{"start": start, "end": end, "day": hdoc_day}]}


def add_hdoc_to_tweets(tweets) -> Dict:
    tweets_data = tweets.get("data", [])
    for tweet in tweets_data:
        text = tweet.get("text", "")
        hdoc_day = get_hdoc_day(PATTERN, text)
        entities = tweet["entities"]
        if hdoc_day:
            entities.update(hdoc_day)
    return tweets


def group_tweets(tweets) -> OD:
    grouped_tweets = OrderedDict()
    for tweet in tweets["data"][::-1]:
        conversation_id = tweet["conversation_id"]
        id = tweet["id"]
        if conversation_id == id:
            grouped_tweets[conversation_id] = [tweet]
        else:
            grouped_tweets[conversation_id].append(tweet)
    for key in sorted(grouped_tweets.keys(), reverse=True):
        grouped_tweets.move_to_end(key)
    return grouped_tweets


def main():
    tweets = get_tweets()
    tweets = add_hdoc_to_tweets(tweets)
    grouped_tweets = group_tweets(tweets)
    out_path = Path("tweets.json")
    out_path.write_text(json.dumps(grouped_tweets))


if __name__ == "__main__":
    main()
