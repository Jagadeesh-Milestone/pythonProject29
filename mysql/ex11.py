#select with  a filter:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='jagadeesh'
)
mycursor=mydb.cursor()
#mycursor.execute('SELECT * FROM users WHERE address="hyderabad"')
#mycursor.execute('SELECT * FROM users WHERE name="hari"')
mycursor.execute('SELECT * FROM users WHERE id=3')
result=mycursor.fetchall()
for i in result:
    print(i)