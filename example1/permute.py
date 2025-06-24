# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 123 124 132 134 142 143
# 213 214 231 234 241 243

# from itertools import permutations

# for item in permutations(range(1, 5), 3):
#     print(*item, sep="")


from collections import defaultdict
from typing import Any


def permute(arr: list[int], size: int):
    if size is None:
        size = len(arr)

    if len(arr) == 0 or len(arr) == 1:
        return [arr]

    result = []
    for i, num in enumerate(arr, start=0):
        without = arr[0:i] + arr[i + 1 :]
        # print(f"{i=}, {num=}, {without=}")
        rest = permute(without, size - 1)
        for nums in rest:
            result.append([num, *nums[0 : size - 1]])

    return result


def permute_backtrace(arr: list[Any], size: int):
    result = []
    path = []
    used = defaultdict(bool)

    def backtrace():
        if len(path) == size:
            # result.append(path.copy())  # ! must copy
            result.append(path[:])
            # result.append([*path])
            # result.append(list(path))
            return

        for item in arr:
            if used[item]:
                continue

            path.append(item)
            used[item] = True
            backtrace()
            used[item] = False
            path.pop()

    backtrace()

    return result


if __name__ == "__main__":
    expected = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 3, 2],
        [1, 3, 4],
        [1, 4, 2],
        [1, 4, 3],
        [2, 1, 3],
        [2, 1, 4],
        [2, 3, 1],
        [2, 3, 4],
        [2, 4, 1],
        [2, 4, 3],
        [3, 1, 2],
        [3, 1, 4],
        [3, 2, 1],
        [3, 2, 4],
        [3, 4, 1],
        [3, 4, 2],
        [4, 1, 2],
        [4, 1, 3],
        [4, 2, 1],
        [4, 2, 3],
        [4, 3, 1],
        [4, 3, 2],
    ]
    actual = permute([1, 2, 3, 4], size=3)
    # print(f"{actual=}")

    # for item in actual:
    #     print(item)

    assert actual == expected

    actual2 = permute_backtrace([1, 2, 3, 4], size=3)

    assert actual2 == expected, f"{actual2=}"
