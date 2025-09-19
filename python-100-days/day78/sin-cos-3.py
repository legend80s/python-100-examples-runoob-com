import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi)
y1 = np.sin(x)
y2 = np.cos(x)

fig = plt.figure(figsize=(10, 4), dpi=120)
plt.plot(x, y1, linewidth=2, marker="*", color="red")
# 用Figure对象的add_axes方法在现有坐标系中嵌套一个新的坐标系，该方法的参数是一个四元组，
# 代表了新坐标系在原坐标系中的位置，前两个值是左下角的位置，后两个值是坐标系的宽度和高度
ax = fig.add_axes((0.595, 0.6, 0.3, 0.25))
ax.plot(x, y2, marker="^", color="blue")
ax = fig.add_axes((0.155, 0.2, 0.3, 0.25))
ax.plot(x, y2, marker="^", color="green")
plt.show()
