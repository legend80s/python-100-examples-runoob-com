import time
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt

# 每月收入
# fmt: off
incomes = np.array([
    9558, 8835, 9313, 14990, 5564, 11227, 11806, 10242, 11999, 11630,
    6906, 13850, 7483, 8090, 9465, 9938, 11414, 3200, 10731, 19880,
    15500, 10343, 11100, 10020, 7587, 6120, 5386, 12038, 13360, 10885,
    17010, 9247, 13050, 6691, 7890, 9070, 16899, 8975, 8650, 9100,
    10990, 9184, 4811, 14890, 11313, 12547, 8300, 12400, 9853, 12890
])

# 每月网购支出
# fmt: off
outcomes = np.array([
    3171, 2183, 3091, 5928, 182, 4373, 5297, 3788, 5282, 4166,
    1674, 5045, 1617, 1707, 3096, 3407, 4674, 361, 3599, 6584,
    6356, 3859, 4519, 3352, 1634, 1032, 1106, 4951, 5309, 3800,
    5672, 2901, 5439, 1478, 1424, 2777, 5682, 2554, 2117, 2845,
    3867, 2962,  882, 5435, 4174, 4948, 2376, 4987, 3329, 5002
])
X = np.sort(incomes).reshape(-1, 1)  # 将收入排序后处理成二维数组
# print(f'{np.argsort(incomes)=}')
y = outcomes[np.argsort(incomes)]    # 将网购支出按照收入进行排序

print(f'{X=}')
print(f'{y=}')

# 创建模型
model = KNeighborsRegressor()

# 训练模型
start = time.perf_counter()
model.fit(X, y)
print(f'fit: {(time.perf_counter() - start) * 1000:.2f}ms')

start = time.perf_counter()
y_pred = model.predict(X)
print(f'predict: {(time.perf_counter() - start) * 1000:.2f}ms')

print(f'{y_pred=}')

# 原始数据散点图
plt.scatter(X, y, color='navy')
# 预测结果折线图
plt.plot(X, y_pred, color='coral')
plt.show()
