"""
리스트 복사
"""
a = [1,2,3]
b = a
print(id(a))	# 메모리 주소값 동일
print(id(b))	# 메모리 주소값 동일
a[1] = 9
print(a)		# 값이 동일하게 변경
print(b)		# 값이 동일하게 변경

a = [1,2,3]
b = a[:]
print(id(a))	# 메모리 주소값 다름
print(id(b))	# 메모리 주소값 다름
a[1] = 9
print(a)		# 값이 별도로 유지
print(b)		# 값이 별도로 유지

# 변수 값 교환
c = 3
d = 5
c, d = d, c
print(c)
print(d)