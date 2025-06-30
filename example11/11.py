from typing import Generator


def rabbit(num: int) -> Generator[int]:
    a, b = 1, 1

    i = 0

    while i < num:
        yield a
        i += 1
        a, b = b, a + b


print(list(rabbit(8)))

print(list(rabbit(8))[0:3])
print(list(rabbit(8))[-3:])
