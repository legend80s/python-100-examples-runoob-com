# https://coderivers.org/matplotlib/matplotlib-chinese-display/

# import matplotlib.pyplot as plt
# import numpy as np

# plt.rcParams["font.family"] = "SimHei"

# x = np.linspace(0, 2 * np.pi, 100)
# y = np.sin(x)

# plt.plot(x, y)
# # Add an annotation
# plt.annotate(
#     "波峰",
#     xy=(np.pi / 2, 1),
#     xytext=(np.pi / 2 + 0.2, 0.8),
#     arrowprops=dict(facecolor="black"),
# )
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "SimHei"

x = np.arange(1, 6)
y = x**2

plt.bar(x, y)
# Set custom tick labels in Chinese
plt.xticks(x, ["一🍎 苹果", "二", "三", "四", "五"])
plt.show()
