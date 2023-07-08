import pymysql
schema_name = "mydb"
# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

user_name = 'john'
user_id = 1

# Inserting data into table
cursor.execute(f"INSERT into mydb.users (name, id) VALUES ('{user_name}', {user_id})")

cursor.close()
conn.close()
