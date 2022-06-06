#import defTest							#	defTest 모듈 전체 사용
#from defTest import ufn_add				#	defTest 모듈 내에서 ufn_add 메소드만 사용
from defTest import ufn_add, ufn_add2	#	defTest 모듈 내에서 ufn_add, ufn_add2 메소드 사용

a = ufn_add(5, 4)
print(a)