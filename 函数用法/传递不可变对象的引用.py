'''
传递参数是不可变对象（例如：int、float、字符串、元组、布尔值），实际传递的还是对象的引用。
在”赋值操作”时，由于不可变对象无法修改，系统会新创建一个对象。
不可变对象有：
数字、字符串、元组、function等
'''

# 参数传递：传递不可变对象的引用
a = 100


def f1(n):
    print("n:", id(n))  # 传递进来的是a对象的地址
    n1 = id(n)
    n = n + 200  # 由于a是不可变对象，因此创建新的对象n
    print("n:", id(n))  # n已经变成了新的对象
    print(n)
    n2 = id(n)
    print(n1 == n2)


f1(a)
print("a:", id(a))
