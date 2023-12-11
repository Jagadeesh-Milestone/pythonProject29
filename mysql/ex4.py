#create table:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='jagadeesh'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE students(name VARCHAR(20), address VARCHAR(20))')
print('one table created successfully')