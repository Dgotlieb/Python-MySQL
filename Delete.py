# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd=‘123', db='table')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Deleting data into table
cursor.execute("DELETE FROM table.users WHERE name = ‘john'")

cursor.close()
conn.close()