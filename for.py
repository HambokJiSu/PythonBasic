print("{0:=^25}".format("전형적인 For문"))
test_list = ["one", "two", "three"]
for i in test_list:
	print(i)

print("{0:=^25}".format("튜플 변수 활용 For문"))
test_list = [(1,2), (3,4), (5,6)]
for (x, y) in test_list:
	print(x + y)

# range 함수
# range(x, y) : x부터 y미만의 숫자를 데이터로 가짐
print(list(range(1, 11)))

print("{0:=^25}".format("range함수 활용 For문"))
iSum = 0
for i in range(1, 11):
	iSum = iSum + i

print(iSum)

print("{0:=^25}".format("range함수 활용 구구단"))
for i in range(2, 10):
	for j in range(1, 10):
		print(f"{i} * {j} = {i*j}" )

print("{0:=^25}".format("List 내포 For문"))
a = [1,2,3,4]
result = []
for i in a:
	result.append(i*5)

print(result)

print("{0:=^25}".format("List 내포 For문으로 변환"))
a = [1,2,3,4]
result = [i * 5 for i in a]

print(result)

print("{0:=^25}".format("List 내포 For문으로 변환 with If문"))
a = [1,2,3,4]
result = [i * 5 for i in a if i < 4]

print(result)