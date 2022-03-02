from hdoc_tracker.patterns import (
    DEMO_PATTERN,
    HDOC_PATTERN,
    MODERN_HDOC_PATTERN,
    SRC_PATTERN,
)
from hdoc_tracker.utils import (
    add_extra_entities_to_tweets,
    get_extra_entities,
    group_tweets,
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
    assert entities == {"modern_day_list": [{"day": "R1D1", "start": 0, "end": 4}]}
    entities = get_extra_entities(pattern, "R2D10 #100DaysOfCode")
    assert entities == {"modern_day_list": [{"day": "R2D10", "start": 0, "end": 5}]}
    entities = get_extra_entities(pattern, "R20D100 #100DaysOfCode")
    assert entities == {"modern_day_list": [{"day": "R20D100", "start": 0, "end": 7}]}
    entities = get_extra_entities(pattern, "R200D100 #100DaysOfCode")
    assert entities == {"modern_day_list": [{"day": "R200D100", "start": 0, "end": 8}]}
    entities = get_extra_entities(pattern, "d1 of #100DaysOfCode")
    assert not entities
    entities = get_extra_entities(pattern, "day 1 of #100DaysOfCode")
    assert not entities


def test_add_extra_entities_to_tweets():
    tweets = {
        "data": [
            {
                "id": 1,
                "conversation_id": 1,
                "text": "day 1 of #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [{"start": 10, "end": 24, "tag": "100DaysOfCode"}]
                },
            }
        ]
    }
    updated_tweets = add_extra_entities_to_tweets(tweets)
    assert updated_tweets == {
        "data": [
            {
                "id": 1,
                "conversation_id": 1,
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
    }
    tweets = {
        "data": [
            {
                "id": 1,
                "conversation_id": 1,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}]
                },
            }
        ]
    }
    updated_tweets = add_extra_entities_to_tweets(tweets)
    assert updated_tweets == {
        "data": [
            {
                "id": 1,
                "conversation_id": 1,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "modern_day_list": [{"day": "R2D1", "start": 0, "end": 4}],
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
    }


def test_group_tweets_with_no_conversation():
    tweets = {
        "data": [
            {
                "id": 2,
                "conversation_id": 2,
                "text": "R2D2 #100DaysOfCode\nContinue learning websec ;)",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "modern_day_list": [{"day": "R2D2", "start": 0, "end": 4}],
                },
            },
            {
                "id": 1,
                "conversation_id": 1,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "modern_day_list": [{"day": "R2D1", "start": 0, "end": 4}],
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
    grouped_tweets = group_tweets(tweets)


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
                    "modern_day_list": [{"day": "R2D1", "start": 0, "end": 4}],
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
    grouped_tweets = group_tweets(tweets)
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
                    "modern_day_list": [{"day": "R2D1", "start": 0, "end": 4}],
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
                    "modern_day_list": [{"day": "R2D1", "start": 0, "end": 4}],
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
    grouped_tweets = group_tweets(tweets)
    print(grouped_tweets)
    assert grouped_tweets == {
        1: [
            {
                "id": 1,
                "conversation_id": 1,
                "text": "R2D1 #100DaysOfCode\nlearn web security basics\nsrc: https://github.com/attomos/web-security-101\ndemo: https://websec-attomos.vercel.app",
                "entities": {
                    "hashtags": [{"start": 5, "end": 19, "tag": "100DaysOfCode"}],
                    "modern_day_list": [{"day": "R2D1", "start": 0, "end": 4}],
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
