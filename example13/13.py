# > 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。


from typing import Generator


def daffodils(n_digits: int) -> list[int]:
    assert n_digits >= 1, f"`n_digits` should >= 1 but found {n_digits}"

    def get_digits(num: int) -> Generator[int]:
        while num:
            yield num % 10
            num = num // 10

    result: list[int] = []

    for num in range(10 ** (n_digits - 1), 10**n_digits - 1):
        digits = get_digits(num)
        total = sum(digit**n_digits for digit in digits)

        # if 1634 == num:
        #     print(num, digits, total)
        # result.append(num) if sum(d**3 for d in get_digits(num)) == num else ...
        # sum(d**3 for d in get_digits(num)) == num and result.append(num)
        if total == num:
            result.append(num)

    return result


def daffodils2(n_digits: int) -> list[int]:
    assert n_digits >= 1, f"`n_digits` should >= 1 but found {n_digits}"

    def get_digits(num: int) -> Generator[int]:
        while num:
            yield num % 10
            num = num // 10

    return [
        num
        for num in range(10 ** (n_digits - 1), 10**n_digits - 1)
        if sum(digit**n_digits for digit in get_digits(num)) == num
    ]


expected = [153, 370, 371, 407]

print(expected)
print(actual := daffodils(3), actual == expected)

print(daffodils(1))
print(daffodils(2))

# 1634，8208，9474
print(daffodils(4))

# 54748，92727，93084
print(daffodils(5))

# 548834
print(daffodils(6))

# print(daffodils(0))

print(daffodils(1) == daffodils2(1))
print(daffodils(2) == daffodils2(2))
print(daffodils(3) == daffodils2(3))
print(daffodils(4) == daffodils2(4))
print(daffodils(5) == daffodils2(5))
