class Student(object):
	def __init__(self, id, name):
		self.__id = id#双下划线代表私有
		self.__name = name
	def set_id(self, id):
		self.__id = id
	def get_id(self):
		return self.__id
	def set_name(self, name):
		self.__name = name
	def get_name(self):
		return self.__name
	def print_name(self):
		print("%s: %s" % (self.__id, self.__name))
Fey = Student("001", "Feynming")
Fey.print_name()
print(Fey.get_name())#直接输Fey.__name报错,因为python解释器对外把__name改成了_Student__name
print(Fey._Student__name)
print("Fey is an object?", isinstance(Fey, object))
print("\'type(Fey)\':", type(Fey))