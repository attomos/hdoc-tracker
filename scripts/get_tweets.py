import json
import os
from pathlib import Path
from typing import Dict, List

import requests
from dotenv import load_dotenv

load_dotenv()


BEARER_TOKEN = os.getenv("BEARER_TOKEN")


def make_request(url, headers, payload, hashtags_filter: List[str] = None) -> Dict:
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {"error": response.json}

    json_response = response.json()
    if hashtags_filter:
        data = json_response["data"]
        filtered_tweets = []
        for tweet in data:
            for ht in tweet.get("entities", {}).get("hashtags", []):
                if ht.get("tag") in hashtags_filter:
                    filtered_tweets.append(tweet)
        return {
            "data": filtered_tweets,
            "meta": json_response.get("meta"),
        }
    return json_response


def get_tweets() -> Dict:
    # TODO: use since_id
    # TODO: remove hard-coded start_time, end_time
    # TODO: setup GitHub Actions to automatically update tweets
    payload = {
        "tweet.fields": "conversation_id,created_at,entities,public_metrics",
        "max_results": 100,
        "exclude": "retweets",
        "start_time": "2022-01-01T00:00:00Z",
        "end_time": "2022-04-01T00:00:00Z",
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


def main():
    tweets = get_tweets()
    out_path = Path("tweets.json")
    out_path.write_text(json.dumps(tweets))


if __name__ == "__main__":
    main()
