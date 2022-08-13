import pymysql

schema_name = "AAAA"

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='AAAAA', passwd='111111', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
statementToExecute = "CREATE TABLE `"+schema_name+"`.`users`(`id` INT NOT NULL,`name` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`));"
cursor.execute(statementToExecute)

cursor.close()
conn.close()
