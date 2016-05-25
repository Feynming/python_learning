#python内置特殊函数
class Teacher(object):
	def __init__(self, name):
		self.name = name
	def __getattr__(self, attr):
		if attr == 'age':
			return 18
s = Teacher('Feynming')
print(s.name)
print(s.age)

#使用枚举类
from enum import Enum, unique
@unique
class Weekday(Enum):
	Sunday=0
	Monday=1
	Tuesday=2
	Wednesday=3
	Thursday=4
	Friday=5
	Saturday=6
day1=Weekday.Sunday
print(day1==Weekday.Sunday)