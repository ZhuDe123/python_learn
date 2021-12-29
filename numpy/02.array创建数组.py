# 导入numpy模块
import numpy as np

# 使用array函数创建一维数组
a = np.array([1, 2, 3, 4])
print("a*********")
print(a)
print(type(a))
print(a.shape)

# 使用array函数创建二维数组
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("b**********")
print(b)
print(type(b))
print(b.shape)

# 使用array函数创建三维数组
c = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print("c**********")
print(c)
print(type(c))
print(c.shape)

# array函数中dtype的使用
d = np.array([3, 4, 5], dtype=float)
print("d**********")
print(d)
print(type(d))
print(d.shape)

# array函数中ndim的使用
print("e***********")
e = np.array([5, 6, 7], dtype=float, ndmin=3)
print(e)
print(e.shape)


