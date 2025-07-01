def reduceNum(n) -> None | list[int]:
    result = []

    if not isinstance(n, int) or n <= 0:
        print("请输入一个正确的数字 !")
        return None
    elif n in [1]:
        return [n]

    while n not in [1]:  # 循环保证递归
        # print(f"outer {n=}")
        for index in range(2, n + 1):
            if n % index == 0:
                n //= index  # n 等于 n//index
                # print(f"in {n=}")
                result.append(index)
                break

    return result


# 90 =  2 * 3 * 3 * 5
print(num := 90, "=", " * ".join(map(str, reduceNum(num) or [])))
# 100 =  2 * 2 * 5 * 5
print(num := 100, "=", " * ".join(map(str, reduceNum(num) or [])))
