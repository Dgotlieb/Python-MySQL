# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd=‘123', db='table')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Updating data inside the table
cursor.execute("UPDATE table.users SET id = '10' WHERE name = ‘john'")

cursor.close()
conn.close()
