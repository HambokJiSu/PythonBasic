print("{0:=^25}".format("Q1 클래스 상속 생성"))
class Calculator:
	def __init__(self):
		self.value = 0

	def add(self, val):
		self.value += val

class UpgradeCalculator(Calculator):
	def minus(self, val):
		self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

print("{0:=^25}".format("Q2 클래스 상속 생성2"))

class MaxLimitCalculator(Calculator):
	def add(self, val):
		self.value += val
		self.value = 100 if self.value > 100 else self.value

cal = MaxLimitCalculator()
cal.add(50)
cal.add(100)

print(cal.value)

print("{0:=^25}".format("Q3 결과 예측"))

print(all([1,2,abs(-3)-3]))	#	False
print(chr(ord('a')) == 'a')	#	True

print("{0:=^25}".format("Q4 filter와 lambda 활용"))

list1 = [1,-3,2,0,-5,6]
list2 = list(filter(lambda i: i > 0, list1))
print(list2)

print("{0:=^25}".format("Q5 10진수 16진수"))
print(hex(234))
print(int('0xea', 16))

print("{0:=^25}".format("Q6 map과 lambda"))
print(list(map(lambda i: i*3, [1,2,3,4])))

print("{0:=^25}".format("Q7 min max"))
print(min([-8, 2, 7, 5, -3, 0, 1]))
print(max([-8, 2, 7, 5, -3, 0, 1]))

print("{0:=^25}".format("Q8 round"))
print(round(17/3, 4))

print("{0:=^25}".format("Q9 round"))
print(round(17/3, 4))

print("{0:=^25}".format("Q15 random"))
list1 = list(range(1, 46))
list2 = []
import random

def pop_number(data):
	number = random.choice(data)
	data.remove(number)
	return number

for i in range(1, 7):
	list2.append(pop_number(list1))

print(list2)