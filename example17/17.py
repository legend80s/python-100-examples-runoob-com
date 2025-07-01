from collections import defaultdict
from typing import DefaultDict, Literal, TypeAlias, TypedDict


class CounterResult(TypedDict):
    char: int
    space: int
    digit: int
    others: int


Category: TypeAlias = Literal["char", "space", "digit", "others"]


def count_category(text: str) -> CounterResult:
    counts: DefaultDict[Category, int] = defaultdict(int)

    for char in text:
        if char.isalpha():
            counts["char"] += 1
        elif char.isspace():
            counts["space"] += 1
        elif char.isdigit():
            counts["digit"] += 1
        else:
            counts["others"] += 1

    return CounterResult(**counts)


# 123runoobc  kdf235*(dfl

# char = 13,space = 2,digit = 6,others = 2
print(count_category("123runoobc  kdf235*(dfl"))
