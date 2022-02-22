from collections import OrderedDict
import re
from typing import Dict
from typing import OrderedDict as OD

from hdoc_tracker.patterns import DEMO_PATTERN, HDOC_PATTERN, PatternConfig, SRC_PATTERN


def get_extra_entities(pc: PatternConfig, text: str):
    if m := re.search(pc.pattern, text):
        if len(m.groups()) == pc.expected_groups_len:
            entity = m.group(pc.target_group_position)
            start, end = m.span(pc.target_group_position)
            if pc.optional_flag and pc.optional_flag_position:
                flag = bool(m.group(pc.optional_flag_position))
                return {
                    f"{pc.key.value}s": [
                        {
                            "start": start,
                            "end": end,
                            pc.key.value: entity,
                            pc.optional_flag: flag,
                        }
                    ]
                }
            return {
                f"{pc.key.value}s": [
                    {
                        "start": start,
                        "end": end,
                        pc.key.value: entity,
                    }
                ]
            }


def add_extra_entities_to_tweets(tweets) -> Dict:
    tweets_data = tweets.get("data", [])
    for tweet in tweets_data:
        text = tweet.get("text", "")
        hdoc_day = get_extra_entities(HDOC_PATTERN, text)
        src = get_extra_entities(SRC_PATTERN, text)
        demo = get_extra_entities(DEMO_PATTERN, text)
        entities = tweet["entities"]
        if hdoc_day:
            entities.update(hdoc_day)
        if src:
            entities.update(src)
        if demo:
            entities.update(demo)
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
