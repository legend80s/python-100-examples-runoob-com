# from typing import assert_type, cast


from typing import Any, TypeVar


def guess_number_adding_to_perfect_square() -> list[int]:
    """

    x + 100 = m^2
    x + 100 + 168 = n^2

    """
    nums: list[int] = []
    for i in range(2, int(168 / 2 + 1)):
        j = 168 / i

        if i > j and i % 2 == 0 and j % 2 == 0:
            # print(i, j)
            m = (i + j) / 2
            x = m**2 - 268
            assert x.is_integer()
            # print(f"{x=}")
            temp = cast(int, x)
            nums.append(temp)
            # print(f"{x=} {math.sqrt(x+100)=} {math.sqrt(x+100+168)=}")

    return nums


def guess_number_adding_to_perfect_square_floor_division() -> list[int]:
    """

    x + 100 = m^2
    x + 100 + 168 = n^2

    """
    nums: list[int] = []
    for i in range(2, int(168 / 2 + 1)):
        if 168 % i != 0:
            continue

        j = 168 // i

        if i > j and i % 2 == 0 and j % 2 == 0:
            m = (i + j) // 2
            x = m**2 - 268
            # print(i, j, m, x)
            nums.append(x)
            # print(f"{x=} {math.sqrt(x+100)=} {math.sqrt(x+100+168)=}")

    return nums


T = TypeVar("T")


def cast(typ: type[T], val: Any) -> T:
    return val


if __name__ == "__main__":
    ints = guess_number_adding_to_perfect_square()

    # print(f"{10.0.is_integer() = }")

    ints2 = guess_number_adding_to_perfect_square_floor_division()

    print(f"{ints=}")
    print(f"{ints2=}")

    assert ints == [-99, 21, 261, 1581], ints
    assert ints2 == [-99, 21, 261, 1581], ints2
