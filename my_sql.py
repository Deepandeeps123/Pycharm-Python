import mysql.connector
mydb=mysql.connector.connect(host="3306",user="root",password="python",database="python1")
# host="Localhost",
#      port="3306",
#      user="root",
#      password="python",
#      database="python1"
query='create database e12'
a=mydb.cursor()
a.execute(query)