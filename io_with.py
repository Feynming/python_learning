#读文件
f = open("ListComprehension.py", 'r', encoding='utf-8')
for l in f.readlines():
	print(l.strip())
f.close()
#with 写文件
with open("test.txt", 'w') as f:
	f.write("hello world\r\nfeynming\r\n")