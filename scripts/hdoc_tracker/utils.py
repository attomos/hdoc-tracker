import json
import re
from collections import OrderedDict, defaultdict
from math import floor
from pathlib import Path
from typing import Any, DefaultDict, Match
from typing import OrderedDict as OD

from deepdiff import DeepDiff

from hdoc_tracker.patterns import (
    DEMO_PATTERN,
    HDOC_PATTERN,
    MODERN_HDOC_PATTERN,
    SRC_PATTERN,
    PatternConfig,
)
from hdoc_tracker.shapes import Tweet

STATS_PATH = Path("./stats.json")


def build_entities(pc: PatternConfig, m: Match):
    entity = m.group(pc.target_group_position)
    start, end = m.span(pc.target_group_position)
    key = pc.key.value
    if key == "modern_day":
        key = "day"
    entities = {
        key: entity,
        "start": start,
        "end": end,
    }
    if pc.optional_flag and pc.optional_flag_position:
        flag = bool(m.group(pc.optional_flag_position))
        entities[pc.optional_flag] = flag
    if pc.details:
        for detail_key, detail_type, detail_index in pc.details:
            if detail_type == "int":
                entities[detail_key] = int(m.group(detail_index))
            else:
                entities[detail_key] = m.group(detail_index)
    return {f"{key}_list": [entities]}


def get_extra_entities(pc: PatternConfig, text: str):
    if m := re.search(pc.pattern, text):
        if len(m.groups()) == pc.expected_groups_len:
            return build_entities(pc, m)


def add_extra_entities_to_tweets(tweets: list[Tweet]) -> list[Tweet]:
    for tweet in tweets:
        text = tweet.get("text", "")
        modern_hdoc_day = get_extra_entities(MODERN_HDOC_PATTERN, text)
        hdoc_day = get_extra_entities(HDOC_PATTERN, text)
        src = get_extra_entities(SRC_PATTERN, text)
        demo = get_extra_entities(DEMO_PATTERN, text)
        entities = tweet["entities"]
        if modern_hdoc_day:
            entities.update(modern_hdoc_day)
        if hdoc_day:
            entities.update(hdoc_day)
        if src:
            entities.update(src)
        if demo:
            entities.update(demo)
    return tweets


def group_tweets_by_conversation_id(tweets) -> OD:
    grouped_tweets: OD[int, list] = OrderedDict(
        {t["conversation_id"]: [] for t in tweets["data"]}
    )
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


def group_tweets_by_round(
    conversations: dict[str, list[Any]]
) -> DefaultDict[str, list[str]]:
    dd: DefaultDict[str, list[str]] = defaultdict(list)
    for conversation, tweets in conversations.items():
        if len(tweets) > 0:
            day_list = tweets[0].get("entities", {}).get("day_list", [{}])
            round_value = day_list[0].get("round_value", 1)
            dd[f"round{round_value}"].append(conversation)
    return dd


def merge_tweets(tweets_json: dict, new_data: dict) -> dict:
    for key in new_data.keys():
        updated_tweets = []
        old_tweets = tweets_json.get(key, [])
        new_tweets = new_data[key]
        merged_tweets = old_tweets + new_tweets
        lookup_dict = {}
        for tweet in merged_tweets:
            id = tweet.get("id")
            if id not in lookup_dict:
                lookup_dict[id] = tweet
        all_tweet_ids = [tweet.get("id") for tweet in merged_tweets]
        sorted_ids = sorted(set(all_tweet_ids))
        for id in sorted_ids:
            if id in lookup_dict:
                updated_tweets.append(lookup_dict[id])
        tweets_json[key] = updated_tweets
    od = OrderedDict(tweets_json)
    for key in sorted(od.keys(), reverse=True):
        od.move_to_end(key)
    return od


def compare_tweets(old_tweets_text, new_tweets_text):
    old_json = json.loads(old_tweets_text)
    new_json = json.loads(new_tweets_text)

    old_count = 0
    new_count = 0
    for k, v in old_json.items():
        old_count += len(v)

    for k, v in new_json.items():
        new_count += len(v)
    return old_count == new_count


def compare_json_string(old_json_str: str, new_json_str: str):
    old_json = json.loads(old_json_str)
    new_json = json.loads(new_json_str)
    diff = DeepDiff(old_json, new_json, ignore_order=True)
    return len(diff.keys()) != 0


def load_stats():
    if STATS_PATH.exists():
        return json.loads(STATS_PATH.read_text())

    return {}


def update_stats(new_stats: str):
    STATS_PATH.write_text(new_stats)


def get_recent_index(arr: list[Any]):
    idx = floor(len(arr) * 0.7)
    if idx < len(arr):
        return idx
    return -1


if __name__ == "__main__":
    text = "R2D1 #100DaysOfCode"
    modern_hdoc_day = get_extra_entities(MODERN_HDOC_PATTERN, text)
    print(modern_hdoc_day)
