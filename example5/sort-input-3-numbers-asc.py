from typing import Generator


def sort_input_numbers1(count: int = 3) -> None:
    nums: list[float] = []

    for idx in range(1, 1 + count):
        try:
            num = float(input(f"输入第 {idx}/{count} 个数: "))
        except ValueError:
            print("请输入数字。\n")
        else:
            # 解决输入 5 输出 5.0 问题
            nums.append(int(num) if num.is_integer() else num)
    print("sorted", sorted(nums))


def sort_input_numbers_re_input_on_error(count: int = 3) -> None:
    nums: list[float] = []
    idx = 1

    while idx < 1 + count:
        try:
            num = float(input(f"输入第 {idx}/{count} 个数: "))
        except ValueError:
            print("请输入数字。\n")
        else:
            # 解决输入 5 输出 5.0 问题
            nums.append(int(num) if num.is_integer() else num)
            idx += 1

    print("sorted", sorted(nums))


def sort_input_numbers_list_comprehension(count: int = 3) -> None:
    floats: list[float] = [
        float(input(f"输入第 {idx}/{count} 个数: ")) for idx in range(1, 1 + count)
    ]
    nums: list[float | int] = [int(num) if num.is_integer() else num for num in floats]

    print("sorted", sorted(nums))


def sort_input_numbers_list_comprehension_one_line(count: int = 3) -> None:
    nums = [
        (
            int(num)
            if (num := float(input(f"输入第 {i}/{count} 个数: "))).is_integer()
            else num
        )
        for i in range(1, count + 1)
    ]

    print("sorted", sorted(nums))


def sort_input_numbers_list_comprehension_generator(count: int = 3) -> None:
    floats: Generator[float, None, None] = (
        float(input(f"输入第 {idx}/{count} 个数: ")) for idx in range(1, 1 + count)
    )

    nums: Generator[float | int] = (
        int(num) if num.is_integer() else num for num in floats
    )

    print("sorted", sorted(nums))


def sort_input_numbers_functional(count: int = 3) -> None:
    floats: map[float] = map(
        lambda idx: float(input(f"输入第 {idx}/{count} 个数: ")), range(1, 1 + count)
    )

    nums: map[float | int] = map(
        lambda num: int(num) if num.is_integer() else num, floats
    )

    print(f"{nums=}")

    print("sorted", sorted(nums))


def sort_input_numbers_functional_2(count: int = 3) -> None:
    nums: map[float | int] = map(
        lambda num: int(num) if num.is_integer() else num,
        map(
            lambda idx: float(input(f"输入第 {idx}/{count} 个数: ")),
            range(1, 1 + count),
        ),
    )

    # print(f"{nums=}")

    print("sorted", sorted(nums))


# sort_input_numbers1(4)

# sort_input_numbers_list_comprehension(3)
sort_input_numbers_list_comprehension_generator(3)
# sort_input_numbers_functional_2(3)
# sort_input_numbers_functional(3)

# print((5.0).is_integer())
# sort_input_numbers_re_input_on_error(3)
