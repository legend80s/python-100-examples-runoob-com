import numpy as np
import matplotlib.pyplot as plt


def normal_pdf(x, mu=0, sigma=1):
    """手动计算正态分布的概率密度函数（PDF）"""
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)


def plot1():
    # 设置参数
    mu, sigma = 0, 1  # 均值和标准差
    x = np.linspace(-5, 5, 1000)  # x轴范围

    # 计算PDF
    pdf = normal_pdf(x, mu, sigma)

    # 绘制图形
    plt.figure(figsize=(10, 6))
    plt.plot(x, pdf, label=f"N(μ={mu}, σ={sigma})", color="blue", linewidth=2)

    # 标记均值和±σ范围
    plt.axvline(mu, color="red", linestyle="--", label="Mean (μ)")
    plt.axvline(mu + sigma, color="green", linestyle=":", label="±1σ")
    plt.axvline(mu - sigma, color="green", linestyle=":")

    # 美化图形
    plt.title("Normal Distribution (Manual Implementation)", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("Probability Density", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


def plot2():
    # 定义不同参数
    params = [
        {"mu": 0, "sigma": 1, "label": "N(0,1)", "color": "blue"},
        {"mu": 2, "sigma": 0.5, "label": "N(2,0.5)", "color": "red"},
        {"mu": -1, "sigma": 1.5, "label": "N(-1,1.5)", "color": "green"},
    ]

    # 绘制对比图
    plt.figure(figsize=(10, 6))
    x = np.linspace(-6, 6, 1000)

    for p in params:
        pdf = normal_pdf(x, p["mu"], p["sigma"])
        plt.plot(x, pdf, label=p["label"], color=p["color"], linewidth=2)

    plt.title("Normal Distributions (Manual Implementation)", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("Probability Density", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


def main():
    plot2()


if __name__ == "__main__":
    main()
