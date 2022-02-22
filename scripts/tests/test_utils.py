from hdoc_tracker.utils import get_extra_entities

from hdoc_tracker.patterns import DEMO_PATTERN, HDOC_PATTERN, SRC_PATTERN


def test_demo_entities():
    entities = get_extra_entities(DEMO_PATTERN, "demo: https://hdoc-tracker.vercel.app")
    assert entities == {
        "demos": [{"start": 6, "end": 18, "demo": "https://hdoc", "fixed": False}]
    }
    entities = get_extra_entities(
        DEMO_PATTERN, "fixed demo: https://hdoc-tracker.vercel.app"
    )
    assert entities == {
        "demos": [{"start": 12, "end": 24, "demo": "https://hdoc", "fixed": True}]
    }
    entities = get_extra_entities(
        DEMO_PATTERN, "Today, I continue to work on the tracker project..."
    )
    assert not entities


# def test_hdoc_entites():


def test_hdoc_entites():
    entities = get_extra_entities(HDOC_PATTERN, "day 1 of #100DaysOfCode")
    assert entities == {"days": [{"day": "day 1", "end": 5, "start": 0}]}
    assert 1 == 0  # testing GitHub Actions
    # entities = get_extra_entities(HDOC_PATTERN, "R2D1 #100DaysOfCode")
    # assert entities == {"days": [{"day": "day 1", "end": 5, "start": 0}]}
    # entities = get_extra_entities(HDOC_PATTERN, "day1 of #100DaysOfCode")
    # assert not entities
