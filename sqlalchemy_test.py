from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义Teacher对象:
class Teacher(Base):
	# 表的名字:
	__tablename__ = 'teacher'

	# 表的结构:
	tid = Column(String(20), primary_key=True)
	tname = Column(String(20))
	 
# 定义Student对象:
class Student(Base):
	# 表的名字:
	__tablename__ = 'student'

	# 表的结构:
	sid = Column(String(20), primary_key=True)
	sname = Column(String(20))
	tid = Column(String(20), ForeignKey('teacher.tid'))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/teacherstudent')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_teacher = Teacher(tid='3', tname='Bob')
# 添加到session:
session.add(new_teacher)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
teacher = session.query(Teacher).filter(Teacher.tid=='5').one()
# 打印类型和对象的name属性:
print('type:', type(teacher))
print('name:', teacher.tname)
# 关闭Session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
students = session.query(Student).filter(Student.tid=='222').all()
# 打印类型和对象的name属性:
print('type:', type(students))
for s in students:
	print("sid:%s, sname:%s, tid:%s" % (s.sid, s.sname, s.tid))
# 关闭Session:
session.close()