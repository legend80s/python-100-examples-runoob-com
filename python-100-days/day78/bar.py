import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"].insert(0, "SimHei")
plt.rcParams["axes.unicode_minus"] = False

x = np.arange(4)
y1 = np.random.randint(20, 50, 4)
y2 = np.random.randint(10, 60, 4)

labels = ["Q1", "Q2", "Q3", "Q4"]

print(f"{x=}")
print(f"{y1=}")
print(f"{y2=}")

plt.figure(figsize=(6, 4), dpi=120)
# plt.bar(x - 0.1, y1, width=0.2, label="销售 A 组")
# plt.bar(x + 0.1, y2, width=0.2, label="销售 B 组")
plt.bar(labels, y1, width=0.4, label="销售 A 组")
plt.bar(labels, y2, width=0.4, bottom=y1, label="销售 A 组")
plt.title("2025 年销售数据")

# plt.xticks(x, labels=["Q1", "Q2", "Q3", "Q4"])

plt.legend(loc="lower right")
# plt.legend()
plt.show()
