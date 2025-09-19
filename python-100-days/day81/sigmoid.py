def my_plot():
    # 画一个 sinmoid 曲线图
    import numpy as np
    import matplotlib.pyplot as plt

    def sigmoid(x: np.ndarray):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(x: np.ndarray):
        s = sigmoid(x)
        return s * (1 - s)

    # 1
    x = np.linspace(-10, 10, 100)
    y = sigmoid(x)
    y2 = sigmoid_derivative(x)

    # 2
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label="Sigmoid Function", color="blue", linewidth=2)
    plt.plot(
        x, y2, label="Derivative of Sigmoid", color="red", linewidth=2, linestyle="--"
    )

    # 3
    plt.title("Sigmoid Function: $\\sigma(z) = \\frac{1}{1 + e^{-z}}$", fontsize=14)
    plt.xlabel("Input (z)", fontsize=12)
    plt.ylabel("Output $\\sigma(z)$", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)  # 网格线
    plt.axhline(y=0.5, color="blue", linestyle=":", label="y=0.5")  # 水平参考线
    plt.axhline(y=0.25, color="red", linestyle=":", label="y=0.25")  # 水平参考线
    plt.legend()

    # 4
    plt.show()


def deepseek1():
    import numpy as np
    import matplotlib.pyplot as plt
    from typing import Tuple

    def sigmoid(x: np.ndarray) -> np.ndarray:
        """计算 Sigmoid 函数值"""
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(x: np.ndarray) -> np.ndarray:
        """计算 Sigmoid 函数的导数"""
        s = sigmoid(x)
        return s * (1 - s)

    def plot_sigmoid_and_derivative() -> Tuple[plt.Figure, plt.Axes]:
        """
        绘制 Sigmoid 函数及其导数

        返回:
            Tuple[plt.Figure, plt.Axes]: 图形和坐标轴对象
        """
        # 创建数据
        x: np.ndarray = np.linspace(-10, 10, 1000)
        y_sigmoid: np.ndarray = sigmoid(x)
        y_derivative: np.ndarray = sigmoid_derivative(x)

        # 创建图形
        fig, ax = plt.subplots(figsize=(10, 6))

        # 绘制 Sigmoid 函数
        ax.plot(x, y_sigmoid, label="Sigmoid Function", color="blue", linewidth=2)

        # 绘制导数
        ax.plot(
            x,
            y_derivative,
            label="Derivative of Sigmoid",
            color="red",
            linewidth=2,
            linestyle="--",
        )

        # 添加图例和标题
        ax.set_title("Sigmoid Function and its Derivative", fontsize=14)
        ax.set_xlabel("x", fontsize=12)
        ax.set_ylabel("f(x)", fontsize=12)
        ax.legend(fontsize=12)

        # 添加网格和调整布局
        ax.grid(True, linestyle="--", alpha=0.6)
        fig.tight_layout()

    # 绘制图形
    plot_sigmoid_and_derivative()
    plt.show()


def main():
    # my_plot()
    deepseek1()


if __name__ == "__main__":
    main()


# import numpy as np
# import matplotlib.pyplot as plt


# # 定义Sigmoid函数
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))


# # 生成x值（从-10到10，间隔0.1）
# x = np.linspace(-10, 10, 100)
# y = sigmoid(x)

# # 绘制图像
# plt.figure(figsize=(8, 4))  # 设置画布大小
# plt.plot(x, y, label="Sigmoid Function", color="blue", linewidth=2)

# # 添加标题和标签
# plt.title("Sigmoid Function: $\\sigma(z) = \\frac{1}{1 + e^{-z}}$", fontsize=14)
# plt.xlabel("Input (z)", fontsize=12)
# plt.ylabel("Output $\\sigma(z)$", fontsize=12)
# plt.grid(True, linestyle="--", alpha=0.6)  # 网格线
# plt.axhline(y=0.5, color="red", linestyle=":", label="y=0.5")  # 水平参考线
# plt.legend()

# # 显示图像
# plt.show()
