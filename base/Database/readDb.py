# 查询记录

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 执行查询语句
values = cursor.fetchall()

print(values)

cursor.close()
conn.close()
