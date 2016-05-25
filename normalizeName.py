#规范化名字
def normalize(name):
		return name.title()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
#利用reduce求list的积
from functools import reduce
def prod(L):
	def p(x, y):
		return x * y
	return reduce(p, L)
print('2 * 4 * 6 * 8 = ',prod([2,4,6,8]))
#'123.456'-->123.456
def str2float(s):
	L = s.split('.')
	def f(x, y):
		return x * 10 + y
	def f2(x, y):
		return x / 10 + y
	def char2num(char):
		return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[char]
	#也可以把f替换为lambda x, y : x *10 + y
	return reduce(f, map(char2num, L[0])) + reduce(f2, map(char2num, L[1][::-1])) / 10
print("str2float('123.456') = ", str2float('123.456'))