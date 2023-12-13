#select all records from table
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='jagadeesh'
)
mycursor=mydb.cursor()
mycursor.execute('SELECT * FROM users')
result=mycursor.fetchall()
for i in result:
    print(i)
