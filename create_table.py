import pymysql

schema_name = "mydb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
statementToExecute = "CREATE TABLE `" + schema_name + "`.`users`(`id` INT NOT NULL,`name` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`));"
cursor.execute(statementToExecute)

cursor.close()
conn.close()
