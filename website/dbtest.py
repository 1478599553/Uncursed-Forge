import pymysql
#连接数据库，创建连接对象connection
#连接对象作用是：连接数据库、发送数据库信息、处理回滚操作（查询中断时，数据库回到最初状态）、创建新的光标对象
connection = pymysql.connect(host = 'localhost' ,user = 'root' ,
                             password = '12434hhmht'  ,
                             db = 'mysql' 
                             )
cur = connection.cursor()
#查看有哪些数据库，通过cur.fetchall()获取查询所有结果
print(cur.fetchall())