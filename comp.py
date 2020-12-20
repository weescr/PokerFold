import operator

class A:
	
	__slots__ = ('test')

	def __init__(self):
		self.test = 1

	def __str__(self):
		return 'A'

	def __eq__(self,other):
		return other.value == self.test

class B:
	__slots__ = ('test')

	def __init__(self):
		self.test = 2

	def __str__(self):
		return 'B'

	def __eq__(self,other):
		return other.value == self.test

obj1 = A()
obj2 = A()
obj3 = A()

obj4 = B()
obj5 = B()
obj6 = B()

n = [obj4, obj1, obj3, obj5, obj2, obj6]

print(set(map(operator.attrgetter('test'), n)))