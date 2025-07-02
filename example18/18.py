from typing import Literal, TypeAlias

Digit: TypeAlias = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]


def sum_nums(n: int, *, digit: Digit) -> int:
    total = 0

    for count in range(1, n + 1):
        total += int(str(digit) * count)

    return total


def sum_nums2(n: int, *, digit: Digit) -> int:
    return sum(int(str(digit) * count) for count in range(1, n + 1))


# 4936
print(sum_nums(4, digit=4))
print(sum_nums2(4, digit=4))
