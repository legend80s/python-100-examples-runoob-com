# import numpy as np
import matplotlib.pyplot as plt

plt.rc("font", family="Microsoft YaHei")
# plt.rcParams["font.family"] = "Segoe UI Emoji, YouYuan"

title = "xx 平台流水线耗时占比 2025-07-03"
data = [140.62, 76.70, 81.68]
labels = [
    "依赖安装时间 Yarn",
    "代码构建时间 umi@2",
    "其他非前端可控时间",
]

plt.figure(figsize=[5, 5], dpi=120)

plt.pie(
    data,
    autopct="%.1f%%",
    radius=1,
    pctdistance=0.8,
    # colors=np.random.rand(7, 3),
    # explode=[0.1, 0, 0],
    # shadow=True,
    textprops=dict(fontsize=8, color="black"),
    wedgeprops=dict(linewidth=1, width=0.55),
    labels=labels,
)

plt.title(title)
plt.show()
