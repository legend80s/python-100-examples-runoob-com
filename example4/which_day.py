def which_day_in_the_year(year: int, month: int, days: int) -> int:
    MONTH_DAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # 31 59 90 120 151 181

    # print(year, month, days)

    previous = sum(MONTH_DAYS[i] for i in range(1, month))

    # print(previous)

    return previous + days + (1 if is_leap_year(year) else 0)


def is_leap_year(year) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


if __name__ == "__main__":
    cases = ((2015, 6, 7, 158),)

    for *date, expected in cases:
        nth = which_day_in_the_year(*date)
        assert nth == expected, f"{nth=}"
    else:
        print("测试成功")
