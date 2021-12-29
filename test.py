from matplotlib import pyplot as plt
# import matplotlib
import numpy as np
# a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

# for i in a:
#     print(i)
#
plt.rcParams['font.family']=['FangSong']

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
plt.plot(x, y)

plt.title("哈哈哈哈")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.show()