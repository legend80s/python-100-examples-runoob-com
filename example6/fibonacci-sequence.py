# 1 0
# 2 1
# 3 1
# 4 2
# 5 3
# 6 5
# 7 8
# 8 13
# 9 21
# 10 34


from itertools import islice, tee
from typing import Generator


def fibonacci_iterator(n: int) -> int:
    a, b = 0, 1

    if n == 1:
        return 0
    if n == 2:
        return 1

    for _ in range(0, n - 2):
        c = a + b
        a = b
        b = c

    return c


def fibonacci_iterator2(n: int) -> int:
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


def fibonacci_generator(n) -> Generator[int, None, int]:
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b

    return a


# for i in range(1, 11):
# print(f"#{i}", fibonacci_iterator2(i))
# print(f"#{i}", fibonacci_iterator(i))

assert list(fibonacci_generator(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print([*fibonacci_generator(10)])

gen1, gen2 = tee(fibonacci_generator(10))

print("the 10th:", next(islice(gen1, 10 - 1, None), None))


# gen = fibonacci_generator(10)
try:
    while True:
        print(next(gen2))
except StopIteration as error:
    print(f"{error.value=}")
# print(list(fibonacci_generator(10)))
