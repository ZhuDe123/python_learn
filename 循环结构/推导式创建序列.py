'''
推导式是从一个或者多个迭代器快速创建序列的一种方法。
它可以将循环和条件判断结合，从而避免冗长的代码。推导式是典型的Python风格，
会使用它代表你已经超过Python初学者的水平。
'''

'''
推导式列表
语法如下：
　　　　[表达式 for item in 可迭代对象]
　　或者 [表达式 for item in 可迭代对象 if  条件判断]
'''
list1 = [x * 2 for x in range(10) if x % 2 == 0]
print("列表")
print(list1)

# 字典推导式
# {key_expression:value_expression  for 表达式 in 可迭代对象}
my_text = 'l love you! I love hzau'
char_count = {c: my_text.count(c) for c in my_text}
print("字典")
print(char_count.items())

# 集合推导式
# {表达式  for 表达式 in 可迭代对象}
b = {x for x in range(1, 101) if x % 3 == 0}
print("集合")
print(b)

# 生成器推导式(生成元组)
'''
(表达式  for 表达式 in 可迭代对象)产生的是一个生成器对象。显然，元组没有推导式
一个生成器只能运行一次。第一次迭代可以得到数据，第二次迭代数据就没有了
'''
print("元组")
gnt = (x for x in range(1, 100) if x % 3 == 0)
for x in gnt:
    print(x, end='\t')
