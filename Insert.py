import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='root', passwd='123', db='SCHEMA_NAME')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into SCHEMA_NAME.users (name, id) VALUES (‘john', 5)")

cursor.close()
conn.close()
