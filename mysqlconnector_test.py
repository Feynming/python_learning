import mysql.connector

try:
	conn = mysql.connector.connect(user='root', password='root', database='teacherstudent')
	cursor = conn.cursor()
	cursor.execute("select * from student")
	values = cursor.fetchall()
	print(values)
finally:
	cursor.close()
	conn.close()
