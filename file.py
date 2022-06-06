print("{0:=^25}".format("파일 생성"))
f = open("새파일.txt", "w")	# r : 읽기 모드, w : 쓰기 모드, a : 추가 모드 (파일의 마지막에 새로운 내용 추가)
f.close()

print("{0:=^25}".format("파일 생성(디렉토리 포함)"))
import os
os.makedirs("./test", exist_ok=True)

f = open("./test/새파일2.txt", "w")
f.close()

print("{0:=^25}".format("파일 생성 후 내용 입력"))
f = open("새파일3.txt", "w")
for i in range(1, 11):
	data = f"{i}번째 줄입니다.\n"
	f.write(data)
f.close()

print("{0:=^25}".format("readline 함수로 파일 읽기"))
f = open("새파일3.txt", "r")	# r : 읽기 모드, w : 쓰기 모드, a : 추가 모드 (파일의 마지막에 새로운 내용 추가)
while True:
	line = f.readline()
	if not line: 
		break
	print(line)
f.close()

print("{0:=^25}".format("readlines 함수로 파일 읽기"))
f = open("새파일3.txt", "r")	# r : 읽기 모드, w : 쓰기 모드, a : 추가 모드 (파일의 마지막에 새로운 내용 추가)
lines = f.readlines()
for line in lines:
	print(line.strip())	#	strip() : 줄 끝의 줄 바꿈 문자를 제거
f.close()

print("{0:=^25}".format("read 함수로 파일 읽기"))
f = open("새파일3.txt", "r")	# r : 읽기 모드, w : 쓰기 모드, a : 추가 모드 (파일의 마지막에 새로운 내용 추가)
data = f.read()
print(data)
f.close()

print("{0:=^25}".format("with문으로 파일 자동 닫기"))
with open("새파일3.txt", "r") as f:
	data = f.read()
	print(data)