class FourCal:
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def add(self):
		return self.first + self.second

a = FourCal(5, 9)
print(a.add())

print(a.first)
print(a.second)

class MoreFourCal(FourCal):	# 클래스 상속은 괄호에 클래스명 기술
	def pow(self):
		return self.first ** self.second

b = MoreFourCal(2, 10)
print(b.pow())