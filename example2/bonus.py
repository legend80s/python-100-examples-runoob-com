def calculate_bonus_if(profit: float) -> float:
    """
    - If the profit is less than or equal to 100,000 yuan, 10% of the commission can be commissioned as a bonus;
    - if the profit i is higher than 100,000 yuan and less than or equal to 200,000 yuan (100,000<≤200,000, the part below 100,000 yuan will be commissioned at 10% , the portion above 100,000 yuan can be commissioned at 7.5%;
    - when 200,000 <i≤400,000, the portion below 200,000 will still be commissioned according to the above method (the same below), and the portion above 200,000 yuan will be commissioned at 5%;
    - 400,000< When i ≤ 600,000, the portion above 400,000 yuan is commissioned at 3%;
    - when 600,000<i ≤ 1,000,000, the portion above 600,000 yuan is commissioned at 1.5%;
    - when i> 1,000,000, the portion exceeding 1 million yuan is commissioned at 1% Commission.
    """
    if profit <= 10e4:
        return profit * 10 / 100

    if profit <= 20e4:
        return (profit - 10e4) * 7.5 / 100 + calculate_bonus_if(10e4)

    if profit <= 40e4:
        return (profit - 20e4) * 5 / 100 + calculate_bonus_if(20e4)

    if profit <= 60e4:
        return (profit - 40e4) * 3 / 100 + calculate_bonus_if(40e4)

    if profit <= 100e4:
        return (profit - 60e4) * 1.5 / 100 + calculate_bonus_if(60e4)

    return (profit - 100e4) * 1 / 100 + calculate_bonus_if(100e4)


def calculate_bonus_switch_case_1(profit: float) -> float:
    """
    题目：企业发放的奖金根据利润提成。

    - 利润(I)低于或等于10万元时，奖金可提10%；
    - 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    - 20万到40万之间时，高于20万元的部分，可提成5%；
    - 40万到60万之间时高于40万元的部分，可提成3%；
    - 60万到100万之间时，高于60万元的部分，可提成1.5%;
    - 高于100万元时，超过100万元的部分按1%提成，

    从键盘输入当月利润I，求应发放奖金总数？
    """
    match True:
        case _ if profit <= 10e4:
            return 0.1 * profit
        case _ if profit <= 20e4:
            return (profit - 10e4) * 7.5 / 100 + calculate_bonus_switch_case_1(10e4)
        case _ if profit <= 40e4:
            return (profit - 20e4) * 5 / 100 + calculate_bonus_switch_case_1(20e4)
        case _ if profit <= 60e4:
            return (profit - 40e4) * 3 / 100 + calculate_bonus_switch_case_1(40e4)
        case _ if profit <= 100e4:
            return (profit - 60e4) * 1.5 / 100 + calculate_bonus_switch_case_1(60e4)
        case _:
            return (profit - 100e4) * 1 / 100 + calculate_bonus_switch_case_1(100e4)


def calculate_bonus_switch_case_2(profit: float) -> float:
    match profit:
        case _ if profit <= 10e4:
            return 0.1 * profit
        case _ if profit <= 20e4:
            return (profit - 10e4) * 7.5 / 100 + calculate_bonus_switch_case_2(10e4)
        case _ if profit <= 40e4:
            return (profit - 20e4) * 5 / 100 + calculate_bonus_switch_case_2(20e4)
        case _ if profit <= 60e4:
            return (profit - 40e4) * 3 / 100 + calculate_bonus_switch_case_2(40e4)
        case _ if profit <= 100e4:
            return (profit - 60e4) * 1.5 / 100 + calculate_bonus_switch_case_2(60e4)
        case _:
            return (profit - 100e4) * 1 / 100 + calculate_bonus_switch_case_2(100e4)


# Bonus calculation
def reward(profit: float) -> float:
    if profit <= 10:
        return profit * 0.1
    elif profit <= 20 and profit > 10:
        return (profit - 10) * 0.075 + 1
    elif profit <= 40 and profit > 20:
        return (profit - 20) * 0.05 + 10 * 0.1 + 10 * 0.075
    elif profit <= 60 and profit > 40:
        return (profit - 40) * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.1
    elif profit <= 100 and profit > 60:
        return (profit - 60) * 0.015 + 20 * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.1
    elif profit > 100:
        return (
            (profit - 100) * 0.01
            + 40 * 0.015
            + 20 * 0.03
            + 20 * 0.05
            + 10 * 0.075
            + 10 * 0.1
        )


def calculate_bonus_deepseek(profit):
    if profit <= 100000:
        return profit * 0.10
    elif profit <= 200000:
        return 100000 * 0.10 + (profit - 100000) * 0.075
    elif profit <= 400000:
        return 100000 * 0.10 + 100000 * 0.075 + (profit - 200000) * 0.05
    elif profit <= 600000:
        return 100000 * 0.10 + 100000 * 0.075 + 200000 * 0.05 + (profit - 400000) * 0.03
    elif profit <= 1000000:
        return (
            100000 * 0.10
            + 100000 * 0.075
            + 200000 * 0.05
            + 200000 * 0.03
            + (profit - 600000) * 0.015
        )
    else:
        return (
            100000 * 0.10
            + 100000 * 0.075
            + 200000 * 0.05
            + 200000 * 0.03
            + 400000 * 0.015
            + (profit - 1000000) * 0.01
        )


# if __name__ == "__main__":
#     profit = float(input("Please enter the current month's profit (ten thousand): "))
#     print(reward(profit) * 10000)


def answer(i: float) -> float:
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0, 6):
        if i > arr[idx]:
            r += (i - arr[idx]) * rat[idx]
            # print((i - arr[idx]) * rat[idx])
            i = arr[idx]
    return r


def italic(text):
    return f"\033[3m{text}\033[0m"


print(f"""
{italic("> 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？")}
""")

# try:
#     profit = float(input("请输入当月利润I（单位元），将计算应发放奖金总数：¥ "))
# except ValueError as err:
#     print("请输入有效的数字", err)
# except KeyboardInterrupt:
#     print(f"\n\n{italic('用户退出')}")
#     pass
# else:
#     print("应发奖金", calculate_bonus(profit))

if __name__ == "__main__":
    cases = [
        # ("80000", 8000.00),
        # ("150000", 13750.00),
        # ("300000", 27500.00),
        # ("500000", 35500.00),
        # ("800000", 41500.00),
        # ("1200000", 43500.00),
        (50000, 5000),
        (100000, 10000),
        (150000, 13750),
        (250000, 20000),
        (450000, 29000),
        (650000, 34250),
        (1200000, 41500),
    ]

    for profit, bonus in cases:
        actual = calculate_bonus_deepseek(profit)
        assert actual == bonus, (
            f"标准答案 deepseek：{actual=}, expected={bonus} when {profit=}"
        )
    else:
        print("标准答案 deepseek 正确")

    for profit, bonus in cases:
        actual = reward(profit / 1e4) * 1e4
        assert actual == bonus, f"标准答案1：{actual=}, expected={bonus} when {profit=}"
    else:
        print("标准答案 1 正确")

    for profit, bonus in cases:
        actual = answer(profit)
        assert actual == bonus, f"标准答案2：{actual=}, expected={bonus} when {profit=}"
    else:
        print("标准答案 2 正确")

    for profit, bonus in cases:
        actual = calculate_bonus_switch_case_1(profit)
        assert actual == bonus, (
            f"自己实现 1：{actual=}, expected={bonus} when {profit=}"
        )
    else:
        print("自己实现 1 正确")

    for profit, bonus in cases:
        actual = calculate_bonus_switch_case_2(profit)
        assert actual == bonus, (
            f"自己实现 2：{actual=}, expected={bonus} when {profit=}"
        )
    else:
        print("自己实现 2 正确")
