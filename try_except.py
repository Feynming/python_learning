#try except finally
try:
	print('try...')
	x = 10 / 0
	print('result:', x)
except ZeroDivisionError as e:
	print("except:", e)
finally:
	print("finally")
print("End...")
#raise
def MyError(ValueError):
	pass
def foo(s):
	n = int(s)
	if n == 0:
		raise MyError("invalid value:%s" % s)
	return 10 / n
foo("0")

