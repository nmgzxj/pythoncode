#coding:utf8
# 使用 Connector/Python 进行查询操作。

import mysql.connector

# 创建连接
config = {
          'user':'root',
          'password':'editedit',
          'host':'127.0.0.1',
          'port':3306,
          'database':'learnsystem'}
conn = mysql.connector.connect(**config)

# 创建游标
cur = conn.cursor()

# 执行查询SQL
sql = "SELECT * FROM tuser"
cur.execute(sql)

# 获取查询结果
result_set = cur.fetchall()
if result_set:
    for row in result_set:
        print "%s, %s, %s, %s" % (row[0],row[3],row[4],row[7])

# 关闭游标和连接
cur.close()
conn.close()