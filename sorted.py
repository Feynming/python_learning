#sorted函数
def by_name(t):
	return sorted(t[0])
L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L1, key=by_name)
print(L2)
#按成绩从高到低排序
def by_score(t):
	return t[1]
L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L1, key=by_score, reverse=True)
print(L2)