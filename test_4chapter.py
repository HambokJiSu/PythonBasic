print("{0:=^25}".format("Q1 자연수 홀/짝 여부 판단 함수"))
def is_odd(n):
	if(n % 2 == 1): print("홀수")
	else : print("짝수")

is_odd(4)

print("{0:=^25}".format("Q2 입력으로 들어오는 모든 수 평균"))
def all_sum(*args):
	sum1 = 0
	for i in args:
		sum1 = sum1 + i
	print(sum1 / len(args))

all_sum(1, 2, 3, 4, 7)

print("{0:=^25}".format("Q3 합계 오류 수정"))
# input1 = input("첫번째 숫자를 입력하세요.")
# input2 = input("두번째 숫자를 입력하세요.")

# total = int(input1) + int(input2)
# print("합은 %s입니다." % total)

print("{0:=^25}".format("Q4 출력 결과가 다른 것"))
# 3번, 띄어쓰기 추가됨

print("{0:=^25}".format("Q5 프로그램 수정"))
with open("test.txt", "w") as f1:
	f1.write("Life is too short")

f2 = open("test.txt", "r")
print(f2.read())
f2.close()

# print("{0:=^25}".format("Q6 사용자의 입력을 파일에 저장"))
# f3 = open("test5.txt", "a")
# input1 = input("추가 내용을 입력하세요.")
# f3.write(input1)
# f3.close()

print("{0:=^25}".format("Q7 파일 내용 수정 저장"))
f7 = open("test7.txt", "r")
data = f7.read()
f7.close()
f7 = open("test7.txt", "w")
f7.write(data.replace("java", "python"))
f7.close()