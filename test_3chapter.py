print("{0:=^25}".format("Q1"))
print("shirt")

print("{0:=^25}".format("Q2"))
i = 1
sum1 = 0
while i <= 1000:
	if(i % 3 == 0):
		sum1 = sum1 + i

	i = i + 1
print(sum1)

print("{0:=^25}".format("Q3"))
i = 1
while i <= 5:
	print("*"*i)
	i = i + 1

print("{0:=^25}".format("Q4"))
for i in range(1, 101):
	print(i, end=" ") if i < 100 else print(i)

print("{0:=^25}".format("Q5"))
list1 = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum1 = 0
for i in list1:
	sum1 = sum1 + i
print(sum1 / len(list1))

print("{0:=^25}".format("Q6"))
numbers = [1,2,3,4,5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)