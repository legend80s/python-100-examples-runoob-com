# %config InlineBackend.figure_format='svg'

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, num=60)
y1, y2 = np.sin(x), np.cos(x)

plt.figure(figsize=(8, 4), dpi=120)

# plt.subplot(1, 2, 1)
plt.subplot(2, 1, 1)
plt.plot(x, y1, linewidth=1, marker="*", color="red")
plt.annotate(
    "sin(x)",
    xytext=(0.5, -0.75),
    xy=(0, -0.25),
    fontsize=12,
    arrowprops={
        "arrowstyle": "->",
        "color": "darkgreen",
        "connectionstyle": "angle3, angleA=90, angleB=0",
    },
)

# plt.subplot(1, 2, 2)
plt.subplot(2, 1, 2)
plt.plot(x, y2, linewidth=1, marker="^", color="blue")
plt.annotate(
    "cos(x)",
    xytext=(-3, 0.75),
    xy=(-1.25, 0.5),
    fontsize=12,
    arrowprops={
        "arrowstyle": "->",
        "color": "darkgreen",
        "connectionstyle": "arc3, rad=0.35",
    },
)

plt.show()
