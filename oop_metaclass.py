#type()创建新的类型(实际上，python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建class)
def hello(self, name='world'):
	print("Hello,%s" % name)
Hello = type('Hello', (object,), dict(hello=hello))
h = Hello()
h.hello()
print("type(Hello):",type(Hello),"type(h):",type(h))