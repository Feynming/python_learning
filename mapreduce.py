#字符串转自然数
from functools import reduce
def str2int(s):
	def f(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	return reduce(f, map(char2num, s))#仔细体会map、reduce的用法
print(str2int('246810'))