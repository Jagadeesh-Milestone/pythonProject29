#delete records.
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='jagadeesh'
)
mycursor=mydb.cursor()
#mycursor.execute('DELETE FROM users WHERE name="hari"')
#mycursor.execute('DELETE FROM users WHERE address LIKE "%ore%"')
mycursor.execute('DELETE FROM users WHERE id=5')

mydb.commit()
print('deleted successfully')
