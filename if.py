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