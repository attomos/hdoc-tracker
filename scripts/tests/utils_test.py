from hdoc_tracker.patterns import (
    DEMO_PATTERN,
    HDOC_PATTERN,
    MODERN_HDOC_PATTERN,
    SRC_PATTERN,
)
from hdoc_tracker.shapes import Tweet
from hdoc_tracker.utils import (
    add_extra_entities_to_tweets,
    get_extra_entities,
    get_recent_index,
    group_tweets_by_conversation_id,
    group_tweets_by_round,
    merge_tweets,
)


def test_demo_entities():
    entities = get_extra_entities(DEMO_PATTERN, "demo: https://hdoc-tracker.vercel.app")
    assert entities == {
        "demo_list": [
            {
                "start": 6,
                "end": 37,
                "demo": "https://hdoc-tracker.vercel.app",
                "fixed": False,
            }
        ]
    }
    entities = get_extra_entities(
        DEMO_PATTERN, "fixed demo: https://hdoc-tracker.vercel.app"
    )
    assert entities == {
        "demo_list": [
            {
                "start": 12,
                "end": 43,
                "demo": "https://hdoc-tracker.vercel.app",
                "fixed": True,
            }
        ]
    }
    entities = get_extra_entities(
        DEMO_PATTERN, "Today, I continue to work on the tracker project..."
    )
    assert not entities


def test_src_entities():
    entities = get_extra_entities(
        SRC_PATTERN, "src: https://github.com/attomos/hdoc-tracker"
    )
    assert entities == {
        "src_list": [
            {
                "start": 5,
                "end": 44,
                "src": "https://github.com/attomos/hdoc-tracker",
                "fixed": False,
            }
        ]
    }
    entities = get_extra_entities(
        SRC_PATTERN, "fixed src: https://github.com/attomos/hdoc-tracker"
    )
    assert entities == {
        "src_list": [
            {
                "start": 11,
                "end": 50,
                "src": "https://github.com/attomos/hdoc-tracker",
                "fixed": True,
            }
        ]
    }
    entities = get_extra_entities(
        SRC_PATTERN, "Today, I continue to work on the tracker project..."
    )
    assert not entities


def test_original_hdoc_entites():
    entities = get_extra_entities(HDOC_PATTERN, "day 1 of #100DaysOfCode")
    assert entities == {"day_list": [{"day": "day 1", "start": 0, "end": 5}]}
    entities = get_extra_entities(HDOC_PATTERN, "day 100 of #100DaysOfCode")
    assert entities == {"day_list": [{"day": "day 100", "start": 0, "end": 7}]}
    entities = get_extra_entities(HDOC_PATTERN, "day1 of #100DaysOfCode")
    assert not entities
    entities = get_extra_entities(HDOC_PATTERN, "d1 of #100DaysOfCode")
    assert not entities
    entities = get_extra_entities(HDOC_PATTERN, "R1D1 of #100DaysOfCode")
    assert not entities


def test_modern_hdoc_entites():
    pattern = MODERN_HDOC_PATTERN
    entities = get_extra_entities(pattern, "R1D1 #100DaysOfCode")
    assert entities == {
        "day_list": [
            {"day": "R1D1", "start": 0, "end": 4, "round_value": 1, "day_value": 1}
        ]
    }
    entities = get_extra_entities(pattern, "R2D10 #100DaysOfCode")
    assert entities == {
        "day_list": [
            {"day": "R2D10", "start": 0, "end": 5, "round_value": 2, "day_value": 10}
        ]
    }
    entities = get_extra_entities(pattern, "R20D100 #100DaysOfCode")
    assert entities == {
        "day_list": [
            {
                "day": "R20D100",
                "start": 0,
                "end": 7,
                "round_value": 20,
                "day_value": 100,
            }
        ]
    }
    entities = get_extra_entities(pattern, "R200D100 #100DaysOfCode")
    assert entities == {
        "day_list": [
            {
                "day": "R200D100",
                "start": 0,
                "end": 8,
                "round_value": 200,
                "day_value": 100,
            }
        ]
    }
    entities = get_extra_entities(pattern, "d1 of #100DaysOfCode")
    assert not entities
    entities = get_extra_entities(pattern, "day 1 of #100DaysOfCode")
    assert not entities


def test_add_extra_entities_to_tweets():
    tweets: list[Tweet] = [
        {
            "id": "1",
            "conversation_id": "1",
            "text": "day 1 of #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
            "entities": {
                "hashtags": [{"start": 10, "end": 24, "tag": "100DaysOfCode"}]
            },
        }
    ]
    updated_tweets = add_extra_entities_to_tweets(tweets)
    assert updated_tweets == [
        {
            "id": "1",
            "conversation_id": "1",
            "text": "day 1 of #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
            "entities": {
                "hashtags": [{"start": 10, "end": 24, "tag": "100DaysOfCode"}],
                "day_list": [{"day": "day 1", "start": 0, "end": 5}],
                "src_list": [
                    {
                        "src": "https://github.com/attomos/web-security-101",
                        "start": 55,
                        "fixed": False,
                        "end": 98,
                    }
                ],
                "demo_list": [
                    {
                        "demo": "https://websec-attomos.vercel.app",
                        "start": 105,
                        "fixed": False,
                        "end": 138,
                    }
                ],
            },
        }
    ]
    tweets = [
        {
            "id": "1",
            "conversation_id": "1",
            "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
            "entities": {"hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}]},
        }
    ]
    updated_tweets = add_extra_entities_to_tweets(tweets)
    assert updated_tweets == [
        {
            "id": "1",
            "conversation_id": "1",
            "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
            "entities": {
                "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                "day_list": [
                    {
                        "day": "R2D1",
                        "start": 0,
                        "end": 4,
                        "round_value": 2,
                        "day_value": 1,
                    }
                ],
                "src_list": [
                    {
                        "src": "https://github.com/attomos/web-security-101",
                        "start": 51,
                        "fixed": False,
                        "end": 94,
                    }
                ],
                "demo_list": [
                    {
                        "demo": "https://websec-attomos.vercel.app",
                        "start": 101,
                        "fixed": False,
                        "end": 134,
                    }
                ],
            },
        }
    ]


def test_group_tweets_with_no_conversation():
    # keep the data key since the function is not used in Mastodon data processing
    tweets = {
        "data": [
            {
                "id": 2,
                "conversation_id": 2,
                "text": "R2D2 #100DaysOfCode\nContinue learning websec ;)",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "day_list": [{"day": "R2D2", "start": 0, "end": 4}],
                },
            },
            {
                "id": 1,
                "conversation_id": 1,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "day_list": [{"day": "R2D1", "start": 0, "end": 4}],
                    "src_list": [
                        {
                            "src": "https://github.com/attomos/web-security-101",
                            "start": 51,
                            "fixed": False,
                            "end": 94,
                        }
                    ],
                    "demo_list": [
                        {
                            "demo": "https://websec-attomos.vercel.app",
                            "start": 101,
                            "fixed": False,
                            "end": 134,
                        }
                    ],
                },
            },
        ]
    }
    grouped_tweets = group_tweets_by_conversation_id(tweets)
    assert grouped_tweets == {
        2: [
            {
                "id": 2,
                "conversation_id": 2,
                "text": "R2D2 #100DaysOfCode\nContinue learning websec ;)",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "day_list": [{"day": "R2D2", "start": 0, "end": 4}],
                },
            }
        ],
        1: [
            {
                "id": 1,
                "conversation_id": 1,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "day_list": [{"day": "R2D1", "start": 0, "end": 4}],
                    "src_list": [
                        {
                            "src": "https://github.com/attomos/web-security-101",
                            "start": 51,
                            "fixed": False,
                            "end": 94,
                        }
                    ],
                    "demo_list": [
                        {
                            "demo": "https://websec-attomos.vercel.app",
                            "start": 101,
                            "fixed": False,
                            "end": 134,
                        }
                    ],
                },
            },
        ],
    }


def test_group_tweets_with_conversation():
    tweets = {
        "data": [
            {
                "id": 2,
                "conversation_id": 2,
                "text": "Add some screenshots",
                "entities": {},
            },
            {
                "id": 1,
                "conversation_id": 1,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "day_list": [{"day": "R2D1", "start": 0, "end": 4}],
                    "src_list": [
                        {
                            "src": "https://github.com/attomos/web-security-101",
                            "start": 51,
                            "fixed": False,
                            "end": 94,
                        }
                    ],
                    "demo_list": [
                        {
                            "demo": "https://websec-attomos.vercel.app",
                            "start": 101,
                            "fixed": False,
                            "end": 134,
                        }
                    ],
                },
            },
        ]
    }
    grouped_tweets = group_tweets_by_conversation_id(tweets)
    assert grouped_tweets == {
        2: [
            {
                "id": 2,
                "conversation_id": 2,
                "text": "Add some screenshots",
                "entities": {},
            }
        ],
        1: [
            {
                "id": 1,
                "conversation_id": 1,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "day_list": [{"day": "R2D1", "start": 0, "end": 4}],
                    "src_list": [
                        {
                            "src": "https://github.com/attomos/web-security-101",
                            "start": 51,
                            "fixed": False,
                            "end": 94,
                        }
                    ],
                    "demo_list": [
                        {
                            "demo": "https://websec-attomos.vercel.app",
                            "start": 101,
                            "fixed": False,
                            "end": 134,
                        }
                    ],
                },
            },
        ],
    }


def test_group_tweets_with_conversation_and_wrong_order():
    tweets = {
        "data": [
            {
                "id": 1,
                "conversation_id": 1,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "day_list": [
                        {
                            "day": "R2D1",
                            "start": 0,
                            "end": 4,
                            "round_value": 2,
                            "day_value": 1,
                        }
                    ],
                    "src_list": [
                        {
                            "src": "https://github.com/attomos/web-security-101",
                            "start": 51,
                            "fixed": False,
                            "end": 94,
                        }
                    ],
                    "demo_list": [
                        {
                            "demo": "https://websec-attomos.vercel.app",
                            "start": 101,
                            "fixed": False,
                            "end": 134,
                        }
                    ],
                },
            },
            {
                "id": 2,
                "conversation_id": 1,
                "text": "Add some screenshots",
                "entities": {},
            },
        ]
    }
    grouped_tweets = group_tweets_by_conversation_id(tweets)
    assert grouped_tweets == {
        1: [
            {
                "id": 1,
                "conversation_id": 1,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "day_list": [
                        {
                            "day": "R2D1",
                            "start": 0,
                            "end": 4,
                            "round_value": 2,
                            "day_value": 1,
                        }
                    ],
                    "src_list": [
                        {
                            "src": "https://github.com/attomos/web-security-101",
                            "start": 51,
                            "fixed": False,
                            "end": 94,
                        }
                    ],
                    "demo_list": [
                        {
                            "demo": "https://websec-attomos.vercel.app",
                            "start": 101,
                            "fixed": False,
                            "end": 134,
                        }
                    ],
                },
            }
        ],
    }


def test_group_tweets_with_mixed_rounds():
    tweets = {
        "data": [
            {
                "id": 2,
                "conversation_id": 2,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [
                        {
                            "start": 5,
                            "end": 19,
                            "tag": "100DaysOfCode",
                        }
                    ],
                    "day_list": [
                        {
                            "day": "R2D1",
                            "start": 0,
                            "end": 4,
                            "round_value": 2,
                            "day_value": 1,
                        }
                    ],
                    "src_list": [
                        {
                            "src": "https://github.com/attomos/web-security-101",
                            "start": 51,
                            "fixed": False,
                            "end": 94,
                        }
                    ],
                    "demo_list": [
                        {
                            "demo": "https://websec-attomos.vercel.app",
                            "start": 101,
                            "fixed": False,
                            "end": 134,
                        }
                    ],
                },
            },
            {
                "id": 1,
                "conversation_id": 1,
                "text": "day 100 of #100DaysOfCode blah blah",
                "entities": {"day_list": [{"day": "day 100", "start": 0, "end": 7}]},
            },
        ]
    }
    grouped_tweets = group_tweets_by_conversation_id(tweets)
    assert grouped_tweets == {
        2: [
            {
                "id": 2,
                "conversation_id": 2,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [
                        {
                            "start": 5,
                            "end": 19,
                            "tag": "100DaysOfCode",
                        }
                    ],
                    "day_list": [
                        {
                            "day": "R2D1",
                            "start": 0,
                            "end": 4,
                            "round_value": 2,
                            "day_value": 1,
                        }
                    ],
                    "src_list": [
                        {
                            "src": "https://github.com/attomos/web-security-101",
                            "start": 51,
                            "fixed": False,
                            "end": 94,
                        }
                    ],
                    "demo_list": [
                        {
                            "demo": "https://websec-attomos.vercel.app",
                            "start": 101,
                            "fixed": False,
                            "end": 134,
                        }
                    ],
                },
            }
        ],
        1: [
            {
                "id": 1,
                "conversation_id": 1,
                "text": "day 100 of #100DaysOfCode blah blah",
                "entities": {"day_list": [{"day": "day 100", "start": 0, "end": 7}]},
            },
        ],
    }


def test_group_tweets_by_round():
    tweets = {
        "data": [
            {
                "id": 4,
                "conversation_id": 3,
                "text": "#100DaysOfCode\nadd more details to this R2D1",
            },
            {
                "id": 3,
                "conversation_id": 3,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [
                        {
                            "start": 5,
                            "end": 19,
                            "tag": "100DaysOfCode",
                        }
                    ],
                    "day_list": [
                        {
                            "day": "R2D1",
                            "start": 0,
                            "end": 4,
                            "round_value": 2,
                            "day_value": 1,
                        }
                    ],
                    "src_list": [
                        {
                            "src": "https://github.com/attomos/web-security-101",
                            "start": 51,
                            "fixed": False,
                            "end": 94,
                        }
                    ],
                    "demo_list": [
                        {
                            "demo": "https://websec-attomos.vercel.app",
                            "start": 101,
                            "fixed": False,
                            "end": 134,
                        }
                    ],
                },
            },
            {
                "id": 2,
                "conversation_id": 1,
                "text": "#100DaysOfCode\n add more details on day 100 :wink:",
            },
            {
                "id": 1,
                "conversation_id": 1,
                "text": "day 100 of #100DaysOfCode blah blah",
                "entities": {"day_list": [{"day": "day 100", "start": 0, "end": 7}]},
            },
        ]
    }
    gt0 = group_tweets_by_conversation_id(tweets)
    gt1 = group_tweets_by_round(gt0)
    assert gt1 == {"round2": [3], "round1": [1]}
    # TODO: to be continued
    # print(gt0)
    # for round, conversation_ids in gt1.items():
    #     print(round)
    #     print({k: v for k, v in gt0.items() if k in conversation_ids})


def test_merge_tweets():
    # easy merge
    old_tweets = {
        "1": [{"id": "1", "conversation_id": "1", "text": "R2D1 #100DaysOfCode 1/100"}]
    }
    new_tweets = {
        "2": [{"id": "2", "conversation_id": "2", "text": "R2D2 #100DaysOfCode 2/100"}]
    }
    merged_tweets = merge_tweets(old_tweets, new_tweets)
    assert merged_tweets == {
        "1": [{"id": "1", "conversation_id": "1", "text": "R2D1 #100DaysOfCode 1/100"}],
        "2": [{"id": "2", "conversation_id": "2", "text": "R2D2 #100DaysOfCode 2/100"}],
    }

    # still easy, but has replies in each conversation
    old_tweets = {
        "1": [
            {"id": "1", "conversation_id": "1", "text": "R2D1 #100DaysOfCode 1/100"},
            {
                "id": "2",
                "conversation_id": "1",
                "text": "comment for R2D1 #100DaysOfCode",
            },
        ]
    }
    new_tweets = {
        "3": [
            {"id": "3", "conversation_id": "3", "text": "R2D2 #100DaysOfCode 2/100"},
            {
                "id": "4",
                "conversation_id": "3",
                "text": "comment for R2D2 #100DaysOfCode",
            },
        ]
    }
    merged_tweets = merge_tweets(old_tweets, new_tweets)
    assert merged_tweets == {
        "1": [
            {"id": "1", "conversation_id": "1", "text": "R2D1 #100DaysOfCode 1/100"},
            {
                "id": "2",
                "conversation_id": "1",
                "text": "comment for R2D1 #100DaysOfCode",
            },
        ],
        "3": [
            {"id": "3", "conversation_id": "3", "text": "R2D2 #100DaysOfCode 2/100"},
            {
                "id": "4",
                "conversation_id": "3",
                "text": "comment for R2D2 #100DaysOfCode",
            },
        ],
    }

    # one conversation_id, but new_tweets has more replies
    old_tweets = {
        "1": [
            {"id": "1", "conversation_id": "1", "text": "R2D1 #100DaysOfCode 1/100"},
            {
                "id": "2",
                "conversation_id": "1",
                "text": "comment for R2D1 #100DaysOfCode",
            },
        ]
    }
    new_tweets = {
        "1": [
            {
                "id": "2",
                "conversation_id": "1",
                "text": "comment for R2D1 #100DaysOfCode",
            },
            {
                "id": "3",
                "conversation_id": "1",
                "text": "another comment for R2D1 #100DaysOfCode",
            },
        ]
    }
    merged_tweets = merge_tweets(old_tweets, new_tweets)
    assert merged_tweets == {
        "1": [
            {"id": "1", "conversation_id": "1", "text": "R2D1 #100DaysOfCode 1/100"},
            {
                "id": "2",
                "conversation_id": "1",
                "text": "comment for R2D1 #100DaysOfCode",
            },
            {
                "id": "3",
                "conversation_id": "1",
                "text": "another comment for R2D1 #100DaysOfCode",
            },
        ],
    }

    # mixed conversation_id and new_tweets are not in the correct order
    old_tweets = {
        "1": [
            {"id": "1", "conversation_id": "1", "text": "R2D1 #100DaysOfCode 1/100"},
            {
                "id": "2",
                "conversation_id": "1",
                "text": "comment for R2D1 #100DaysOfCode",
            },
        ],
        "4": [
            {"id": "4", "conversation_id": "4", "text": "R2D2 #100DaysOfCode"},
            {
                "id": "5",
                "conversation_id": "4",
                "text": "comment 1 of R2D2 #100DaysOfCode",
            },
        ],
    }
    new_tweets = {
        "1": [
            {
                "id": "7",
                "conversation_id": "1",
                "text": "more comment for R2D1 #100DaysOfCode",
            },
        ],
        "4": [
            {
                "id": "6",
                "conversation_id": "4",
                "text": "comment 2 of R2D2 #100DaysOfCode",
            },
        ],
    }
    merged_tweets = merge_tweets(old_tweets, new_tweets)
    assert merged_tweets == {
        "1": [
            {"id": "1", "conversation_id": "1", "text": "R2D1 #100DaysOfCode 1/100"},
            {
                "id": "2",
                "conversation_id": "1",
                "text": "comment for R2D1 #100DaysOfCode",
            },
            {
                "id": "7",
                "conversation_id": "1",
                "text": "more comment for R2D1 #100DaysOfCode",
            },
        ],
        "4": [
            {"id": "4", "conversation_id": "4", "text": "R2D2 #100DaysOfCode"},
            {
                "id": "5",
                "conversation_id": "4",
                "text": "comment 1 of R2D2 #100DaysOfCode",
            },
            {
                "id": "6",
                "conversation_id": "4",
                "text": "comment 2 of R2D2 #100DaysOfCode",
            },
        ],
    }


def test_get_recent_index():
    arr = []
    idx = get_recent_index(arr)
    assert idx == -1

    arr = [1]
    idx = get_recent_index(arr)
    assert idx == 0

    arr = [1, 2]
    idx = get_recent_index(arr)
    assert idx == 1

    arr = [1, 2, 3]
    idx = get_recent_index(arr)
    assert idx == 2

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    idx = get_recent_index(arr)
    assert idx == 7
