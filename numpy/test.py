# 导入numpy模块
import numpy as np

t1 = np.arange(12).reshape(3, 4).astype("float")
t1[1, 2, :]
print(t1)
