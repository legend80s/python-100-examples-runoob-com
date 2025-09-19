import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """计算 Softmax 函数值"""
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / e_x.sum(axis=axis, keepdims=True)


def plot_softmax_2d() -> Tuple[plt.Figure, plt.Axes]:
    """
    绘制二维输入的 Softmax 函数（适用于二分类）

    返回:
        Tuple[plt.Figure, plt.Axes]: 图形和坐标轴对象
    """
    # 创建数据（假设第二个类分数固定为0）
    x1: np.ndarray = np.linspace(-10, 10, 100)
    x: np.ndarray = np.column_stack([x1, np.zeros_like(x1)])  # 第二个维度固定为0

    # 计算 Softmax
    y: np.ndarray = softmax(x, axis=1)

    # 创建图形
    fig, ax = plt.subplots(figsize=(10, 6))

    # 绘制两个类别的概率
    ax.plot(x1, y[:, 0], label="Class 1 Probability", color="blue", linewidth=2)
    ax.plot(x1, y[:, 1], label="Class 2 Probability", color="red", linewidth=2)

    # 添加图例和标题
    ax.set_title("Softmax Function (2D Input)", fontsize=14)
    ax.set_xlabel("Class 1 Score (Class 2 Score fixed at 0)", fontsize=12)
    ax.set_ylabel("Probability", fontsize=12)
    ax.legend(fontsize=12)

    # 添加网格和调整布局
    ax.grid(True, linestyle="--", alpha=0.6)
    fig.tight_layout()

    return fig, ax


# 绘制二维 Softmax
fig_2d, ax_2d = plot_softmax_2d()
plt.show()
