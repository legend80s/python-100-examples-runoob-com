import numpy as np


# Sigmoid 激活函数及其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# 输入数据
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])  # XOR 问题

# 初始化权重
np.random.seed(1)
# w1=array([[4.17022005e-01, 7.20324493e-01], [1.14374817e-04, 3.02332573e-01]])
w1 = np.random.rand(2, 2)  # 输入层 → 隐藏层

# w2=array([[0.14675589], [0.09233859]])
w2 = np.random.rand(2, 1)  # 隐藏层 → 输出层
print(f"{w2=}")
print(f"{w1=}")
# raise StopIteration
output = None

# 训练
epochs = int(1e4)
# for epoch in range(epochs):
for epoch in range(epochs + 1):
    # 前向传播
    hidden = sigmoid(np.dot(X, w1))
    output = sigmoid(np.dot(hidden, w2))

    # 反向传播
    error = y - output
    d_output = error * sigmoid_derivative(output)
    d_hidden = d_output.dot(w2.T) * sigmoid_derivative(hidden)

    # 更新权重
    w2 += hidden.T.dot(d_output)
    w1 += X.T.dot(d_hidden)

    if epoch % 1000 == 0:
        print(f"{hidden=}")
        print(f"{output=}")
        print(f"{error=}")
        print(f"{d_output=}")
        print(f"{d_hidden=}")
        print(f"{w2=}")
        print(f"{w1=}")

# 10000
#  [[0.03295304]
#  [0.93052381]
#  [0.93052373]
#  [0.09263959]]
print("最终预测结果：\n", output)

# 10e4
# [[0.00671528]
#  [0.97996806]
#  [0.97996806]
#  [0.02695409]]
