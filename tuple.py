"""
튜플과 리스트의 차이점

0. 선언된 값을 바꿀 수 없다
1. 한 개의 요소를 가질 경우 뒤에 콤마 필수
2. 2개 이상의 요소일 경우 괄호 생략 가능
"""
t1 = ()
print(t1)
t2 = (1,)
print(t2)
t3 = (1,2,3)
print(t3)
t4 = 1,2,3
print(t4)
t5 = t2 + t3	#	리스트와 같이 연산도 가능
print(t5)