import pymysql

# 创建与数据库的连接
db = pymysql.connect(host='localhost', user='root', password='zds13938431145', database='pythontest', charset="utf8")
# 创建游标对象cursor
cursor = db.cursor()
# 插入sql语句
sql = '''
    insert into student(sname,sex,age,score) values(%s,%s,%s,%s)
'''
args = [('王五', 'woman', 22, 98.6), ('赵六', 'man', 21, 99.1)]
try:
    # 执行sql语句
    cursor.executemany(sql, args)
    # 提交事务
    db.commit()
    print('插入成功')
except Exception as e:
    print(e)
    # 如果出现异常，回滚
    db.rollback()
    print('插入失败')
finally:
    # 关闭数据库连接
    db.close()
