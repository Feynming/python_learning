import re

#someone@Gmail.com
#bill.gates@microsoft.com
#邮箱判别正则表达式
mailMatcher = re.compile(r'^[\w\.-]+@([\w]+)(\.\w+){1,2}$')
for email in ['someone@Gmail.com', 'bill.gates@microsoft.com', 'feynming@fudan.edu.com']:
	print(mailMatcher.match(email).group(1))

#从形如<Tom Paris> tom@voyager.org的邮箱里取出姓名
def getNameFromEmail(mail):
	mailMatcher2 = re.compile(r'^<(\w+\s+\w+)>(\s+)([\w\.-]+)@(\w+)(\.\w+){1,3}$')
	print(mailMatcher2.match(mail).group(1))
getNameFromEmail('<Tom Paris> tom@voyager.org')