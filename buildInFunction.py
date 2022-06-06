abs(-3)	#	절대값 반환

#	all
r1 = all([1,2,3,4,5,6])	#	반복 가능 자료형이 모두 참인 경우만 True 반환
print("r1 : " + str(r1))
r2 = all([0,2,3,4,5,6])	#	반복 가능 자료형이 모두 참인 경우만 True 반환
print("r2 : " + str(r2))

#	any : 어느 하나가 참일 경우 True

#	chr : 해당 유니코드에 맞는 문자 반환

#	dir : 해당 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌

#	enumerate : 자료형을 입력받아 인덱스를 포함하는 자료형으로 반환
for i, name in enumerate(['aa', 'bb', 'cc']):
	print(i, name)