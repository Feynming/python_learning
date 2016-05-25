#单元测试用的自己实现的dict
class MyDict(dict):
	def __init__(self, **kw):
		super().__init__(**kw)
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:#r"'Dict' object has no attribute '%s'" %key
			raise AttributeError(r"'Dict' object has no attribute '%s'" %key)
	def __setattr__(self, key, value):
		self[key] =value
