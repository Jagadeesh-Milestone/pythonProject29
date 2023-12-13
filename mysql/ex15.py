#delete table:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='jagadeesh'
)
mycursor=mydb.cursor()
mycursor.execute('DROP table employees')
#delete only if table exists
mycursor.execute('DROP table IF EXISTS employees')
print('table dropped successfully')