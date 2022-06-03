"""
집합 자료형 특징

1. 중복 불가
2. 순서 없음
"""
s1 = set([1,2,3])
print(s1)
s2 = set("Hello")	#	중복 제거 확인
print(s2)

s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7])
s3 = s1 & s2		#	교집합
print(s3)
s4 = s1 | s2		#	합집합
print(s4)
s5 = s1 - s2		#	차집합
print(s5)
s1.add(9)			#	단일 값 추가
print(s1)
s1.update([7,8,9])	#	복수 값 추가
print(s1)
s1.remove(9)		#	특정 값 제거
print(s1)