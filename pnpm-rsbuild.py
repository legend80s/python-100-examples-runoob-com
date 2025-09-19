import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体支持
plt.rcParams["font.sans-serif"] = ["SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# 数据准备
scenarios = ["yarn + umi", "pnpm + rsbuild\n第1次", "pnpm + rsbuild\n第2次"]
install_build_times = [54, 29, 15]  # 安装+构建耗时(秒)
total_times = [167, 63, 55]  # 流水线总耗时(秒)
percentages = [32, 46, 27]  # 安装+构建耗时占比(%)

# 创建图表
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# 左侧子图：时间对比
x = np.arange(len(scenarios))
width = 0.35

bars1 = ax1.bar(
    x - width / 2,
    install_build_times,
    width,
    label="安装+构建耗时 (s)",
    color="#FF9999",
)
bars2 = ax1.bar(
    x + width / 2, total_times, width, label="流水线总耗时 (s)", color="#66B2FF"
)

ax1.set_xlabel("构建场景")
ax1.set_ylabel("耗时 (秒)")
ax1.set_title("不同构建场景的时间对比")
ax1.set_xticks(x)
ax1.set_xticklabels(scenarios)
ax1.legend()

# 在柱状图上添加数值标签
for bar in bars1:
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width() / 2.0,
        height + 1,
        f"{height}s",
        ha="center",
        va="bottom",
    )

for bar in bars2:
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width() / 2.0,
        height + 1,
        f"{height}s",
        ha="center",
        va="bottom",
    )

# 右侧子图：占比对比柱状图
bars3 = ax2.bar(scenarios, percentages, color="#99CC99")
ax2.set_xlabel("构建场景")
ax2.set_ylabel("百分比 (%)")
ax2.set_title("安装+构建耗时占比对比")
ax2.set_ylim(0, 50)

# 在柱状图上添加百分比标签
for bar in bars3:
    height = bar.get_height()
    ax2.text(
        bar.get_x() + bar.get_width() / 2.0,
        height + 1,
        f"{height}%",
        ha="center",
        va="bottom",
    )

# 美化图表
plt.suptitle(
    "构建工具迁移性能对比: yarn+umi → pnpm+rsbuild", fontsize=16, fontweight="bold"
)
plt.tight_layout()

plt.show()
