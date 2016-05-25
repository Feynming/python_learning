#hashlib封装了一些常用的摘要算法，如MD5，SHA1等
import hashlib
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def cacl_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode("utf-8"))
	return md5.hexdigest()

def login(user, password):
	if(db[user] == cacl_md5(password)):
		return True
	else:
		return False
print(login('michael', '123456'))



#加盐md5，对用户的简单密码加以保护
def get_md5_salted(password, user):
	return cacl_md5(password + user + "the-Salt")
#注册函数	
def register():
	user = input("请输入用户名:")
	password = input("请输入密码:")
	db[user] = get_md5_salted(password, user)
#加盐登录
def login_salted():
	user = input("请输入用户名:")
	password = input("请输入密码:")
	if(user not in db):
		print("用户不存在...")
		return False
	if(db[user] == get_md5_salted(password, user)):
		print("登录成功")
		return True
	else:
		print("登录失败")
		return False
def main():
	print("开始注册...")
	register()
	print("开始登录...")
	login_salted()

if __name__ == '__main__':
	main()