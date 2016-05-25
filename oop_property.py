#@property
class Student(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self, score):
		if not isinstance(score, int):
			raise ValueError('score value is not int!')
		if score < 0 or score > 100:
			raise ValueError('score value must between 0~100')
		self._score=score
s = Student()
s.score=60
print(s.score)
#s.score=1000
#练习题
class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self, width):
		self._width = width
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self, height):
		self._height = height
	@property
	def resolution(self):
		return self._width * self._height
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution