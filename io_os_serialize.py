#打印当前目录下.py文件的数量
import os
print(len([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]==".py"]))

#json序列化与反序列化
import json
class Student(object):
	def __init__(self, id, name, age):
		self.id = id
		self.name = name
		self.age = age
	#打印类
	def __str__(self):
		return "Student Object:[id:%s, name:%s, age:%s]" %(self.id, self.name, self.age)

def stu2json(stu):
	return {
		"id" : stu.id,
		"name" : stu.name,
		"age" : stu.age
	}
#json的dumps方法用来序列化
print(json.dumps(Student("001", "Feynming", "18"), default=stu2json))
#或者把默认序列化方法指向对象的__dict方法
print(json.dumps(Student("001", "Feynming", "18"), default=lambda obj : obj.__dict__))

def dict2stu(d):
	return Student(d["id"], d["name"], d["age"])
jsonStr = '{"id" : "007", "name" : "james", "age" : "29"}'
#loads和object_hook方法反序列化
print(json.loads(jsonStr, object_hook = dict2stu))
