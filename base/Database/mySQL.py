
# 导入MySQL驱动:
import pymysql

# 注意把password设为你的root口令:
conn = pymysql.connect("localhost","root","1234libinte","test" )
cursor = conn.cursor()

# 创建user表
cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')

# 插入一行记录, 注意Mysql的占位符是%s
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount

# 提交事务:
conn.commit()
cursor.close()

# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

cursor.close()
conn.close