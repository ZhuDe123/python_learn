"""
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
"""

import pymysql

db = pymysql.connect(host="localhost",user="root",password="zds13938431145",database="pythontest",charset="utf8")

cursor = db.cursor()

sql = "select * from student where age >= 23"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        sno=row[0]
        sname=row[1]
        sex=row[2]
        age=row[3]
        score=row[4]

        print('sno:',sno,'sname:',sname,'sex:',sex,'age:',age,'score:',score)
except Exception as e:
    print(e)
    print("查询失败")
finally:
    db.close()