import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='root', passwd='123', db='SCHEMA_NAME')

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM SCHEMA_NAME.users;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()
