#dict常用api(大括号)
d={'fey':'飞','ming':'明'}
#print(d)
print(d.get('fey'))
d['sun']='孙'
print(d)
for (k,v) in d.items():
	print("key:",k,"value:",v)
#set
s=set(range(10))
print(s)
l=['fey','ming','sun','n']
t=set(s.upper() for s in l if isinstance(s,str))
print(t)
t.add('HA')

from collections import Iterable
print(isinstance((),Iterable))
print("abs is",abs)