
'''
可迭代对象
Python包含以下几种可迭代对象：
1.序列。包含：字符串、列表、元组
2.字典
3.迭代器对象（iterator）
4.生成器函数（generator）
5.文件对象
'''
# 遍历一个元组或列表
for x in (20, 30, 40):
    print(x * 3)

# 遍历字符串中的字符
for x in "sxt001":
    print(x)

# 遍历字典
d = {'name': 'gaoqi', 'age': 18, 'address': '西三旗001号楼'}
for x in d:  # 遍历字典所有的key
    print(x)

for x in d.keys():  # 遍历字典所有的key
    print(x)

for x in d.values():  # 遍历字典所有的value
    print(x)

for x in d.items():  # 遍历字典所有的"键值对"
    print(x)

# 打印如下图案
for x in range(5):
    for y in range(5):
        print(x, end="\t")
    print()  # 仅用于换行

# 利用嵌套循环打印九九乘法表
for m in range(1, 10):
    for n in range(1, m + 1):
        print("{0}*{1}={2}".format(m, n, (m * n)), end="\t")
    print()

# 用列表和字典存储下表信息，并打印出表中工资高于15000的数据
r1 = dict(name="高小一", age=18, salary=30000, city="北京")
r2 = dict(name="高小二", age=19, salary=20000, city="上海")
r3 = dict(name="高小三", age=20, salary=10000, city="深圳")
tb = [r1, r2, r3]
for x in tb:
    if x.get("salary") > 15000:
        print(x)
