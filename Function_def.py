import math
def quadratic(a, b, c):
	if b*b-4*a*c<0:
		print("无解")
	elif b*b-4*a*c==0:
		return -b/(2*a)
	else:
		x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)#求根公式
		x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
		return x1,x2
print(quadratic(2, 3, 1)) # => (-0.5, -1.0)