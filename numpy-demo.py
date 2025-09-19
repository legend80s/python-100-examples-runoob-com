# import numpy as np


# # 定义目标函数（损失函数）
# def mse_loss(y_true, y_pred):
#     return np.mean((y_true - y_pred) ** 2)


# # 定义梯度
# def gradient(X, y, theta):
#     return -2 * X.T @ (y - X @ theta) / len(y)


# # 梯度下降算法
# def gradient_descent(X, y, step_size, num_iterations):
#     theta = np.zeros(X.shape[1])  # 初始位置
#     for i in range(num_iterations):
#         grad = gradient(X, y, theta)  # 当前位置的梯度
#         theta -= step_size * grad  # 根据梯度和步伐大小更新位置
#         if i % 100 == 0:
#             loss = mse_loss(y, X @ theta)  # 计算当前高度（损失值）
#             print(f"Iteration {i}, Loss: {loss}")
#     return theta


# # 示例数据
# X = np.array([[1, 2], [2, 3], [3, 4]])  # 地形
# y = np.array([3, 5, 7])  # 目标位置
# step_size = 0.01  # 初始步伐大小
# num_iterations = 1000  # 爬山的步数

# # 开始爬山
# theta = gradient_descent(X, y, step_size, num_iterations)
# print("Trained parameters:", theta)


# import numpy as np


# # 定义损失函数
# def mse_loss(y_true, y_pred):
#     return np.mean((y_true - y_pred) ** 2)


# # 定义梯度
# def gradient(X, y, theta):
#     return -2 * X.T @ (y - X @ theta) / len(y)


# # 梯度下降算法
# def gradient_descent(X, y, learning_rate, num_iterations):
#     theta = np.zeros(X.shape[1])
#     for i in range(num_iterations):
#         grad = gradient(X, y, theta)
#         theta -= learning_rate * grad
#         if i % 100 == 0:
#             loss = mse_loss(y, X @ theta)
#             print(f"Iteration {i}, Loss: {loss}")
#     return theta


# # 示例数据
# X = np.array([[1, 2], [2, 3], [3, 4]])
# y = np.array([3, 5, 7])

# # 尝试不同的学习率
# learning_rates = [1e-4, 1e-3, 1e-2]
# num_iterations = 1000

# for lr in learning_rates:
#     print(f"Training with learning rate: {lr}")
#     theta = gradient_descent(X, y, lr, num_iterations)
#     print("Trained parameters:", theta)

# Training with learning rate: 0.0001
# Trained parameters: [0.74920265 1.0769846 ]

# Training with learning rate: 0.001
# Trained parameters: [0.81108371 1.13091908]

# Training with learning rate: 0.01
# Trained parameters: [0.91847345 1.05649794]

names = ["关羽", "张飞", "赵云", "马超", "黄忠"]
courses = ["语文", "数学", "英语"]
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# scores = list(map(lambda _: [None] * len(courses), names))
scores = [[None] * len(courses) for _ in range(len(names))]
# scores = [[None] * len(courses)] * len(names)
print(scores)
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f"请输入{name}的{course}成绩: "))
        print(scores)
