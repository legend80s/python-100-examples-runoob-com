import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体支持
plt.rcParams["font.sans-serif"] = ["SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# 数据准备
scenarios = ["yarn + umi", "pnpm + rsbuild 第1次", "pnpm + rsbuild 第2次"]
install_build_times = [54, 29, 15]  # 安装+构建耗时(秒)
total_times = [167, 63, 55]  # 流水线总耗时(秒)
percentages = [32, 46, 27]  # 安装+构建耗时占比(%)

# 创建图表
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

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

# 右侧子图：占比对比
colors = ["#FF9999", "#66B2FF", "#99FF99"]
wedges, texts, autotexts = ax2.pie(
    percentages, labels=scenarios, autopct="%1.0f%%", colors=colors, startangle=90
)
ax2.set_title("安装+构建耗时占比对比")

# 美化图表
plt.suptitle(
    "构建工具迁移性能对比: yarn+umi → pnpm+rsbuild", fontsize=16, fontweight="bold"
)
plt.tight_layout()

# 添加统计信息
improvement_text = f"""
性能提升统计:
- 安装+构建耗时减少: {(54 - 15) / 54 * 100:.1f}% (从54s降至15s)
- 流水线总耗时减少: {(167 - 55) / 167 * 100:.1f}% (从167s降至55s)
- 第二次构建比第一次更快: {(29 - 15) / 29 * 100:.1f}% (得益于pnpm缓存)
"""
plt.figtext(
    0.1,
    0.02,
    improvement_text,
    fontsize=12,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgray"),
)

plt.show()
