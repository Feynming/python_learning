#切片 slice
l=['Feynming','Micheal','Melissa','Jordan','Katherine']
#前三个
print(l[:3])
#前三个数，每两个取一个
print(l[:3:2])
#从第一个到-1个，不包括-1
print(l[:-1])
#取倒数三个
print(l[-3:])
#逆转list
print(l[::-1])
#step为负表示反向
print(l[3:0:-1])