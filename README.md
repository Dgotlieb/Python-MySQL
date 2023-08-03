# Python-MySQL
A quick start using PyMySQL

### Inside Pycharm terminal:
``` bash
$ pip install pymysql
$ pip install cryptography
```

-------------------------------------

### From your host's terminal:
Mac / Linux users  
``` bash
mkdir mysql && cd mysql
docker run --name mysql -v $(pwd):/var/lib/mysql -e MYSQL_ROOT_PASSWORD=mysql -e MYSQL_DATABASE=mydb -e MYSQL_USER=user -e MYSQL_PASSWORD=password -p 3306:3306 -d mysql:8.0.33
```
  
Windows users (CMD)  
``` bash
mkdir mysql && cd mysql
docker run --name mysql -v %cd%:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=mysql -e MYSQL_DATABASE=mydb -e MYSQL_USER=user -e MYSQL_PASSWORD=password -p 3306:3306 -d mysql:8.0.33
```
