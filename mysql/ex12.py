#wildcard characters
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='jagadeesh'
)
mycursor=mydb.cursor()
#ursor.execute('SELECT * FROM users WHERE address LIKE "%i%" ')
mycursor.execute('SELECT * FROM users WHERE name LIKE "%sh%" ')

result=mycursor.fetchall()
for i in result:
    print(i)