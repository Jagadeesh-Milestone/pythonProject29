#create a new database
import  mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha'
)
cursor=mydb.cursor()
cursor.execute('CREATE DATABASE milestone1')
print('one database created successfully')
