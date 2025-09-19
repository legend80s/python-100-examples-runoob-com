import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """计算 Softmax 函数值"""
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / e_x.sum(axis=axis, keepdims=True)


def plot_softmax_3d() -> tuple[plt.Figure, Axes3D]:
    """
    绘制三维输入的 Softmax 函数（适用于三分类）

    返回:
        Tuple[plt.Figure, Axes3D]: 图形和3D坐标轴对象
    """
    # 创建数据（固定第三个类分数为0）
    x1: np.ndarray = np.linspace(-5, 5, 50)
    x2: np.ndarray = np.linspace(-5, 5, 50)
    x1_grid, x2_grid = np.meshgrid(x1, x2)
    x: np.ndarray = np.dstack(
        [x1_grid, x2_grid, np.zeros_like(x1_grid)]
    )  # 第三个维度固定为0

    # 计算 Softmax
    y: np.ndarray = softmax(x, axis=2)

    # 创建3D图形
    fig = plt.figure(figsize=(14, 10))

    # 绘制三个类别的概率
    titles: List[str] = [
        "Class 1 Probability",
        "Class 2 Probability",
        "Class 3 Probability",
    ]
    colors: List[str] = ["red", "green", "blue"]

    for i in range(3):
        ax = fig.add_subplot(1, 3, i + 1, projection="3d")
        surf = ax.plot_surface(
            x1_grid, x2_grid, y[:, :, i], cmap="viridis", edgecolor="none"
        )
        ax.set_title(titles[i], fontsize=12)
        ax.set_xlabel("Class 1 Score", fontsize=10)
        ax.set_ylabel("Class 2 Score", fontsize=10)
        ax.set_zlabel("Probability", fontsize=10)
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    fig.suptitle("Softmax Function (3D Input - Class 3 Score fixed at 0)", fontsize=14)
    fig.tight_layout()

    return fig, ax


# 绘制三维 Softmax
fig_3d, ax_3d = plot_softmax_3d()
plt.show()
