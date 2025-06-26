from copy import copy, deepcopy
from typing import TypeVar


array = ["1", "2", "3"]

a1 = array[:]
print("01", a1 == array, a1 is array, a1)  # True False

a2 = array.copy()
print("02", a2 == array, a2 is array, a2)  # True False

a3 = deepcopy(array)
print("03", a3 == array, a3 is array, a3)  # True False


T = TypeVar("T")


def copy1(arr: list[T]) -> list[T]:
    return [item for item in arr]


a4 = copy1(array)
print("04", a4 == array, a4 is array, a4)  # True False


def copy2(arr: list[T]) -> list[T]:
    result = []
    for item in arr:
        result.append(item)

    return result


print("05", (a5 := copy2(array)) == array, a5 is array, a5)  # True False


def copy3(arr: list[T]) -> list[T]:
    result = []
    result.extend(arr)
    return result


print("06", (a6 := copy3(array)) == array, a6 is array, a6)  # True False


def copy7(arr: list[T]) -> list[T]:
    return list(arr)


print("07", (a7 := copy7(array)) == array, a7 is array, a7)  # True False


def copy8(arr: list[T]) -> list[T]:
    return [*arr]


print("08", (a8 := copy8(array)) == array, a8 is array, a8)  # True False


def copy9(arr: list[T]) -> list[T]:
    return copy(arr)


print("09", (a9 := copy9(array)) == array, a9 is array, a9)  # True False


def copy10(arr: list[T]) -> list[T]:
    def identity(x):
        return x

    return list(map(identity, arr))


print(10, (a10 := copy10(array)) == array, a10 is array, a10)  # True False


def copy11(arr: list[T]) -> list[T]:
    # return arr * 2
    return 1 * arr


print(11, (a11 := copy11(array)) == array, a11 is array, a11)  # True False
