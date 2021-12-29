import pymysql

# 创建与数据库的连接
db = pymysql.connect(host='localhost', user='root', password='zds13938431145', database='pythontest',charset="utf8")
try:

    # 创建游标对象cursor
    cursor = db.cursor()
    # 使用execute()方法执行sql，如果表存在则删除
    cursor.execute('drop table if EXISTS student')
    # 创建表的sql
    sql = '''
        create table student(
        sno int(8) primary key auto_increment,
        sname varchar(30) not null,
        sex varchar(5) ,
        age int(2),
        score float(3,1)
        )
    '''
    cursor.execute(sql)
except:
    print('创建表失败')
finally:
    # 关闭数据库连接
    db.close()
