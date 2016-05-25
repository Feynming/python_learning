#列表生成式
L1=['Hello','World',18,'Apple',None,'feynming']
L2=[s.lower() for s in L1 if isinstance(s,str)]
print(L2)

#杨辉三角
def triangles(n):
	a=0
	N=[1]
	while a < n:
		yield N
		N.append(0)
		N = [N[i-1]+N[i] for i in range(len(N))]
		a += 1
	return 'done'
	
t = triangles(10)
while True:
	try:
		x = next(t)
		print("t:",x)
	except StopIteration as e:
		print(e.value)
		break
	
