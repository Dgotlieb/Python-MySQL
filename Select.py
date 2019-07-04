# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd=‘123', db='table')

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM table.users;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()
