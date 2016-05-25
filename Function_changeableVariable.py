#可变参数
def calc(*numbers):#*是可变参数的标识
	sum=0
	for n in numbers:
		sum += n*n
	return sum
print(calc(1,2,3,4,5))
print(calc())
nums=[1,2,3,4]
print(calc(*nums))

#关键字参数和命名关键字参数
def person(name, age, **kw):#kw是关键字参数，**是标识
	print('name:', name, 'age:', age, 'other:', kw)
person('feynming', 24)
person('feynming',18,city='shanghai')
person('feynming', 18,city="xian",job='student')

def person(name, age, *, job, city):#'*'作为特别分隔符，job和city是命名关键字参数
	print('name:', name, 'age:', age, 'job:', job, 'city:', city)
person('feynming', 24,  city='shanghai',job='engineer')#命名关键字参数传参的时候要写参数名字