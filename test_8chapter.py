print("{0:=^25}".format("Q1 문자열 바꾸기"))
a = "a:b:c:d"
list1 = a.split(":")
b = "#".join(list1)
print(b)

print("{0:=^25}".format("Q2 딕셔너리 값 추출하기"))
try:
	a = {"A":90, "B":80}
	print(a["C"])
except:
	print("70")

print("{0:=^25}".format("Q3 리스트의 더하기와 extend 함수"))
a = [1,2,3]
a += [4,5]
print(a)

print("{0:=^25}".format("Q4 리스트 총합 구하기"))
#	50점 이상 점수의 총합 구하기
a = [20,55,67,82,45,33,90,87,100,25]
iSum = 0
for i in a:
	if i >= 50:
		iSum += i

print(iSum)

print("{0:=^25}".format("Q5 피보나치 함수"))
#	0	1	1	2	3	5	8	13	21

def ufn_pn(n):
	preNum = 0
	curNum = 1
	print(preNum)
	print(curNum)
	while preNum + curNum <= n:
		print(preNum + curNum)
		curNum += preNum
		preNum = curNum - preNum
		
ufn_pn(15)

print("{0:=^25}".format("Q6 숫자의 총합 구하기"))

# input1 = input("숫자를 콤마로 구분하여 입력하세요 : ")
# list1 = input1.split(",")
# iSum = 0
# for i in list1 : iSum += int(i)
# print(iSum)

print("{0:=^25}".format("Q7 한 줄 구구단"))
# input1 = input("구구단을 출력할 숫자를 입력하세요(2~9) : ")
# for i in range(1, 10) : print(i * int(input1), end=" ")

print("{0:=^25}".format("Q8 역순 저장"))
f = open("abc.txt", "r")
list1 = f.readlines()
f.close()

list1.reverse()
f = open("abc.txt", "w")
for i in list1 : f.write(i)
f.close()

print("{0:=^25}".format("Q9 Txt파일 읽고 결과 Txt파일 저장"))
f = open("sample.txt", "r")
list1 = f.readlines()
list2 = []
f.close()

iSum = 0
for i in list1 : iSum += int(i)

f = open("result.txt", "w")
f.write("Total : " + str(iSum))
f.write("\nAverage : " + str(iSum / len(list1)))
f.close()

print("{0:=^25}".format("Q10 사칙연산 계산기"))