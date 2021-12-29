# else语句
'''
while、for循环可以附带一个else语句（可选）。如果for、while语句没有被break语句结束，则会执行else子句，否则不执行。语法格式如下：
    while  条件表达式：
        循环体
    else:
        语句块

或者：
    for  变量  in  可迭代对象：
        循环体
    else:
        语句块
'''
# 员工一共4人。录入这4位员工的薪资。全部录入后，打印提示“您已经全部录入4名员工的薪资”。
# 最后，打印输出录入的薪资和平均薪资
salarySum = 0
salarys = []
for i in range(4):
    s = input("请输入一共4名员工的薪资（按Q或q中途结束）")
    print("i={0}".format(i))
    if s.upper() == 'Q':
        print("录入完成，退出")
        break
    if float(s) < 0:
        # i -= 1
        continue

    salarys.append(float(s))
    salarySum += float(s)

else:
    print("您已经全部录入4名员工的薪资")

print("录入薪资：", salarys)
print("平均薪资{0}".format(salarySum / 4))
