print("{0:=^25}".format("Q1 문자열 바꾸기"))
a = "a:b:c:d"
list1 = a.split(":")
b = "#".join(list1)
print(b)

print("{0:=^25}".format("Q2 딕셔너리 값 추출하기"))
#	내 풀이
# try:
# 	a = {"A":90, "B":80}
# 	print(a["C"])
# except:
# 	print("70")
#	모범 답안
a = {"A":90, "B":80}
print(a.get("C", 70))	# get 함수의 default value 기능 활용

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

class Calculator:

	def __init__(self, pList):
		self.pList = pList	#	self는 Calculator 클래스 선언자 ex) a = Calculator() 에서 a에 해당

	def sum(self):
		iSum = 0
		for i in self.pList : iSum += i
		return iSum

	def avg(self):
		iSum = 0
		for i in self.pList : iSum += i
		return iSum / len(self.pList)

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())

print("{0:=^25}".format("Q11 모듈 사용 방법"))
#	mymod 모듈 사용 방법
#	import mymod
#	from mymod import *
#	from mymod import 열거

print("{0:=^25}".format("Q12 오류와 예외 처리"))
print("7, 첫행에서 Index Error가 유발되어 다른 예외는 무시되고 finally가 수행되어 3과 4가 추가됨")

print("{0:=^25}".format("Q13 DashInsert 함수"))
#	홀수가 연속되면 두 수 사이에 -를 추가하고 짝수가 연속되면 *를 추가하는 기능
# input1 = input("숫자로된 문자열 입력 : ")

# def DashInsert(pStr):
# 	char1 = "-"
# 	char2 = "*"
# 	mod1 = -1
# 	mod2 = -1
# 	rtn = ""
# 	for i in range(1, len(pStr)):
# 		print(pStr[i-1] + " : " + pStr[i])
# 		mod1 = int(pStr[i - 1]) % 2
# 		mod2 = int(pStr[i]) % 2

# 		if(mod1 + mod2 == 0 or mod1 + mod2 == 2):
# 			rtn += pStr[i - 1] + (char1 if mod1 + mod2 == 2 else char2)
# 		else:
# 			rtn += pStr[i - 1]

# 		if(i == len(pStr) - 1):
# 			rtn += pStr[i]
		
# 	print(rtn)

# DashInsert(input1)

print("{0:=^25}".format("Q14 문자열 압축하기"))
# input1 = input("문자열 입력 : ")

# def DataZip(pStr):
# 	prevCnt = 0
# 	prevChar = ""
# 	rtn = ""
# 	for i in range(0, len(pStr)):
# 		print(pStr[i])
# 		if prevChar == "":
# 			prevChar = pStr[i]
# 			prevCnt = 1
# 			continue

# 		if prevChar == pStr[i]:
# 			prevCnt += 1
# 		else:
# 			rtn += prevChar + str(prevCnt)
# 			prevChar = pStr[i]
# 			prevCnt = 1

# 		if i == len(pStr) - 1:
# 			rtn += pStr[i] + str(prevCnt)

# 	print(rtn)

# DataZip(input1)

print("{0:=^25}".format("Q15 숫자 중복 확인"))
# listInput = input("숫자 문자열 입력 : ").split(" ")

# def isNonDuplicate(pStr):
# 	bResult = True

# 	if len(pStr) != 10:
# 		print(False)
# 	else:
# 		for i in range(0, 10):
# 			#print(str(i),":",pStr[i])
# 			if str(i) != pStr[i] : 
# 				bResult = False
# 				break
# 		print(bResult)

# for i in listInput : isNonDuplicate(i)

print("{0:=^25}".format("Q16 모스 부호 해독"))
#	알파벳 별 분기 처리, 공백 1개는 다음 글자, 공백 2개는 띄어쓰기
#	세부 로직은 생략
#	모범 답안 : 알파벳 별 분기가 아닌 Dict 활용, 실제로 구현해보자

print("{0:=^25}".format("Q17 정규식"))
#	1번?

print("{0:=^25}".format("Q18 문자열 검색"))
#	2 + 7 = 9

print("{0:=^25}".format("Q19 그루핑"))

print("{0:=^25}".format("Q20 전방 탐색"))