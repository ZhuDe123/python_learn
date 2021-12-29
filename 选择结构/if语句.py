num = input("输入一个数字：")
if int(num) < 10:
    print(num)
if 3:  # 整数作为条件表达式
    print("ok")
if -1:
    print("0不可以可以成为True")
a = []  # 列表作为条件表达式，由于为空列表，是False
if a:
    print("空列表，False")
s = "False"  # 非空字符串，是True
if s:
    print("非空字符串，是True")

c = 9
if 3 < c < 20:
    print("3<c<20")
if 3 < c and c < 20:
    print("3<c  and c<20")

if True:  # 布尔值
    print("True")

num = input("输入一个数字：")
if int(num) < 10:
    print(num)
else:
    print("数字太大")
# 第二种写法
num = input("请输入一个数字")
print(num if int(num) < 10 else "数字太大")
