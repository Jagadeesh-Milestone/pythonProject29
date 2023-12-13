#primary key:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='jagadeesh'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), address VARCHAR(30))')
print('one table created successfully')