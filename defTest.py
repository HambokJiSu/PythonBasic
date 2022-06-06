def ufn_add(a, b=5):
	return a + b

ufn_add2 = lambda a, b: a + b

if(__name__ == "__main__"):	#	직접 이 파일을 수행했을 때만 정의하는 동작, 모듈로 호출시에는 동작하지 않음
	print("{0:=^25}".format("1"))
	# 함수 초기값 설정 가능
	a = ufn_add(3)
	print(a)

	print("{0:=^25}".format("2"))
	#	lambda : 보통 함수를 한줄로 간결하게 만들 때 사용
	#	return 없이 동작
	result = ufn_add2(3, 4)
	print(result)