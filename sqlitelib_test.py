import os, sqlite3
#__file__获得模块所在的路径
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
print(os.path.dirname(__file__))
print(db_file)
if os.path.isfile(db_file):
	os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

#得到分数在low和high区间的所有学生名字
def get_score(low, high):
	conn = sqlite3.connect(db_file)
	c = conn.cursor()
	c.execute("select name from user where score <= ? and score >= ? order by score asc", (high, low))
	result = c.fetchall()
	#print(result)
	c.close()
	conn.close()
	return [x[0] for x in result]

assert get_score(80, 95) == ['Adam']
assert get_score(60, 80) == ['Bart', 'Lisa']
assert get_score(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score(60, 100)

print("pass")
	
