def find_prime_numbers(start: int, stop: int) -> list[int]:
    def is_prime(num: int) -> bool:
        divisible = any(num % i == 0 for i in range(2, num))

        return not divisible

    return [num for num in range(start, stop + 1) if is_prime(num)]


def find_prime_numbers2(start: int, stop: int) -> list[int]:
    def is_prime(num: int) -> bool:
        divisible = any(num % i == 0 for i in range(2, int(num**0.5) + 1))

        return not divisible

    return [num for num in range(start, stop + 1) if is_prime(num)]


result = find_prime_numbers(101, 200)

print(len(result))
print(result)


expected = [
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    # The total is 21
]

assert result == expected, result
result2 = find_prime_numbers2(101, 200)
print(result2)
assert len(result2) == len(expected), f"{len(expected)=} {len(result2)=} {result2=}"
assert result2 == expected, f"{result2=}"
