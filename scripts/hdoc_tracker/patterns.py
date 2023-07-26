import re
from dataclasses import dataclass
from enum import Enum
from typing import List, Pattern, Tuple


class PatternKey(Enum):
    day = "day"
    modern_day = "modern_day"
    src = "src"
    demo = "demo"


@dataclass
class PatternConfig:
    key: PatternKey
    pattern: Pattern
    expected_groups_len: int
    target_group_position: int
    optional_flag: (str | None) = None
    optional_flag_position: (int | None) = None
    details: (List[Tuple[str, str, int]] | None) = None


HDOC_PATTERN = PatternConfig(
    key=PatternKey.day,
    pattern=re.compile(r"(([Dd]ay \d{1,3}) of) #100DaysOfCode"),
    expected_groups_len=2,
    target_group_position=2,
)
MODERN_HDOC_PATTERN = PatternConfig(
    key=PatternKey.modern_day,
    pattern=re.compile(r"((R(\d{1,}))(D(\d{1,3}))) #100DaysOfCode"),
    expected_groups_len=5,
    target_group_position=1,
    details=[("round_value", "int", 3), ("day_value", "int", 5)],
)
MODERN_HDOC_PATTERN2 = PatternConfig(
    key=PatternKey.modern_day,
    pattern=re.compile(r"#100DaysOfCode ((R(\d{1,}))(D(\d{1,3})))"),
    expected_groups_len=5,
    target_group_position=1,
    details=[("round_value", "int", 3), ("day_value", "int", 5)],
)
DEMO_PATTERN = PatternConfig(
    key=PatternKey.demo,
    pattern=re.compile(r"(fixed )?demo: ([\w\.\/:-]+)"),
    expected_groups_len=2,
    target_group_position=2,
    optional_flag="fixed",
    optional_flag_position=1,
)
SRC_PATTERN = PatternConfig(
    key=PatternKey.src,
    pattern=re.compile(r"(fixed )?src: ([\w\.\/:-]+)"),
    expected_groups_len=2,
    target_group_position=2,
    optional_flag="fixed",
    optional_flag_position=1,
)
