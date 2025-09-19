import random
import statistics
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np

plt.rc("font", family="Kaiti")

# 每月收入
# fmt: off
x: list[float] = [9558, 8835, 9313, 14990, 5564, 11227, 11806, 10242, 11999, 11630,
     6906, 13850, 7483, 8090, 9465, 9938, 11414, 3200, 10731, 19880,
     15500, 10343, 11100, 10020, 7587, 6120, 5386, 12038, 13360, 10885,
     17010, 9247, 13050, 6691, 7890, 9070, 16899, 8975, 8650, 9100,
     10990, 9184, 4811, 14890, 11313, 12547, 8300, 12400, 9853, 12890]

# 每月网购支出
# fmt: off
y: list[float] = [3171, 2183, 3091, 5928, 182, 4373, 5297, 3788, 5282, 4166,
     1674, 5045, 1617, 1707, 3096, 3407, 4674, 361, 3599, 6584,
     6356, 3859, 4519, 3352, 1634, 1032, 1106, 4951, 5309, 3800,
     5672, 2901, 5439, 1478, 1424, 2777, 5682, 2554, 2117, 2845,
     3867, 2962,  882, 5435, 4174, 4948, 2376, 4987, 3329, 5002]



def plot(*, a: float, b: float):
    plt.figure(figsize=(8, 4), dpi=120)
    x_ny = np.array(x)
    y_ny = np.array(y)
    plt.scatter(x_ny, y_ny)
    plt.plot(x_ny, x_ny * a + b, color='r', linewidth=4)
    plt.xlabel('月收入')
    plt.ylabel('月网购支出')

    # plt.title("$y = X \\times 113 + 500$")
    # plt.title("$\\sigma(z) = \\frac{1}{1 + e^{-z}}$")

    plt.title(f'回归模型 $y = {a}\\times X { f' + {b}' if b > 0 else f' - {abs(b)}' if b < 0 else ''}$')
    plt.show()

def get_loss(*, X: list[float], y: list[float], a: float, b: float):
    '''损失函数 - 均方误差

    Args:
        X_: 回归模型的自变量
        y_: 回归模型的因变量
        a_: 回归模型的斜率
        b_: 回归模型的截距

    Returns:
        MSE（均方误差）
    '''
    y_predicated = [a * x + b for x in X]
    
    return statistics.mean([(v1 - v2) ** 2 for v1, v2 in zip(y, y_predicated)])

def calculate_linear_regression() -> tuple[float, float]:
    min_loss = float('inf')
    a = 0.0
    b = 0.0

    for _ in range(int(10e4)):
        # [0, 1)
        temp_a = random.random()
        # [-4000, 4000)
        temp_b = random.random() * 8000 - 4000
        if (loss := get_loss(X=x, y=y, a=a, b=b)) < min_loss:
            print(f'{loss=}')
            min_loss = loss
            a = temp_a
            b = temp_b
    
    print(f'MSE = {min_loss}')

    return a, b

def main():
    # plot(0.514, -1400)
    # MSE = 805287.9080285326
    # a=0.676768227897897
    # b=-1721.3235074984623
    # a, b = calculate_linear_regression()

    # x_bar, y_bar = np.mean(x), np.mean(y)
    # a = np.dot((x - x_bar), (y - y_bar)) / np.sum((x - x_bar) ** 2)
    # b = y_bar - a * x_bar
    a, b = np.polyfit(x, y, deg=1)
    print(f'{a = }, {b = }')

    print(f'{a=}')
    print(f'{b=}')
    plot(a=a, b=b)
    # plot(0.676768227897897, -1721.3235074984623)


if __name__ == "__main__":
    main()
