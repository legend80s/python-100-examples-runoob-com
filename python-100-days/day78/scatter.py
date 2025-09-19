import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"].insert(0, "SimHei")
plt.rcParams["axes.unicode_minus"] = False

x = np.array([5550, 7500, 10500, 15000, 20000, 25000, 30000, 40000])
y = np.array([800, 1800, 1250, 2000, 1800, 2100, 2500, 3500])

plt.figure(figsize=(6, 4), dpi=120)
plt.scatter(x, y)

# properties = {"fontproperties": "SimHei"}
# plt.title("散点图", properties)
# plt.xlabel("坐标 1", properties)
# plt.ylabel("坐标 2", properties)

plt.title("散点图")
plt.xlabel("坐标 1")
plt.ylabel("坐标 2")

plt.show()
