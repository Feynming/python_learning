#筛选法找出所有素数
def primes():
	yield 2
	it = odd()
	while True:
		n = next(it)
		yield n
		it = filter(divisible(n), it)
#构造数列
def odd():
	n=1
	while True:
		n=n+2
		yield n
#筛选n的所有倍数
def divisible(n):
	return lambda x : x % n > 0
#测试
for n in primes():
	if n < 1000:
		print(n)
	else:
		break
#回文数
def is_palindrome(n):
	return lambda n : n == int(str(n)[::-1])
out = filter(is_palindrome(n), range(1, 1000))
print(list(out))
		