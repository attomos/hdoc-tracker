import re
from dataclasses import dataclass
from enum import Enum
from typing import Pattern


class PatternKey(Enum):
    hdoc = "day"
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


HDOC_PATTERN = PatternConfig(
    key=PatternKey.hdoc,
    pattern=re.compile(r"(([Dd]ay \d{1,3}) of|R\d{1,2}D\d{1,3}) #100DaysOfCode"),
    expected_groups_len=2,
    target_group_position=2,
)
DEMO_PATTERN = PatternConfig(
    key=PatternKey.demo,
    pattern=re.compile(r"(fixed )?demo: ([\w\.\/:]+)"),
    expected_groups_len=2,
    target_group_position=2,
    optional_flag="fixed",
    optional_flag_position=1,
)
SRC_PATTERN = PatternConfig(
    key=PatternKey.src,
    pattern=re.compile(r"(fixed )?src: ([\w\.\/:]+)"),
    expected_groups_len=2,
    target_group_position=2,
    optional_flag="fixed",
    optional_flag_position=1,
)
