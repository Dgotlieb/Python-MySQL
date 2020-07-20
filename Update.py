import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='root', passwd='123', db='SCHEMA_NAME')

conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Updating data inside the table
cursor.execute("UPDATE SCHEMA_NAME.users SET id = '10' WHERE name = 'john'")

cursor.close()
conn.close()
