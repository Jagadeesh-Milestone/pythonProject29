#select particular column from a table:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='jagadeesh'
)
mycursor=mydb.cursor()
mycursor.execute('SELECT name,address FROM users')
result=mycursor.fetchall()
for i in result:
    print(i)