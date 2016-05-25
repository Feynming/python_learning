#decorator
def log(func):
	def wrapper(*args, **kw):
		print("begin call")
		r = func(*args, **kw)
		print("end call")
		return r
	return wrapper

import time
@log
def now():
	print(time.strftime('%Y-%m-%d %H:%M:%S'))
now()
	