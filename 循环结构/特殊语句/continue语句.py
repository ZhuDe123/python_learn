# continue语句
'''
continue语句用于结束本次循环，继续下一次。多个循环嵌套时，continue也是应用于最近的一层循环。
'''
# 要求输入员工的薪资，若薪资小于0则重新输入。最后打印出录入员工的数量和薪资明细，以及平均薪资
empNum = 0
salarySum = 0
salarys = []
while True:
    s = input("请输入员工的薪资（按Q或q结束）")

    if s.upper() == 'Q':
        print("录入完成，退出")
        break
    if float(s) < 0:
        continue
    empNum += 1
    salarys.append(float(s))
    salarySum += float(s)

print("员工数{0}".format(empNum))
print("录入薪资：", salarys)
print("平均薪资{0}".format(salarySum / empNum))
