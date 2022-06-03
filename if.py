print("1"+"="*20)
b1 = 1 > 0
if b1:
	print("참")
else:
	print("거짓")

print("2"+"="*20)
b2 = True
b3 = False
if b2 or b3:
	print("OR 성립")
else:
	print("OR 성립 실패")

print("3"+"="*20)
b2 = True
b3 = False
if b2 and b3:
	print("AND 성립")
else:
	print("AND 성립 실패")

print("4"+"="*20)
if 1 in [1,2,3]:
	print("in 성립")
else:
	print("in 성립 실패")

print("5"+"="*20)
if 1 not in [1,2,3]:
	print("not in 성립")
else:
	print("not in 성립 실패")

print("6"+"="*20)
if 1 > 0:
	pass #조건문에서 아무일도 일어나지 않게
else:
	print("거짓")

print("7"+"="*20)
if 1 > 0:pass 		#한 줄로 표현하기
else:print("거짓")	#한 줄로 표현하기

print("8"+"="*20)
i1 = 5
if i1 > 9:
	print("9보다 큼")
elif i1 > 5:	# else if 사용법 : elif
	print("5보다 큼")
elif i1 > 3:
	print("3보다 큼")
else:
	print("3이하")

print("9"+"="*20)
i2 = 7
print("7이야" if i2 == 7 else "7아니야")	# 타 프로그래밍 언어 i2 == 7 ? "7이야" : "7 아니야"