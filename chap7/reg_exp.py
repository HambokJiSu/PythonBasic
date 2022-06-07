"""
문자 클래스 []

[abc] : a, b, c 중 한 개의 문자와 매치
"a" 		: a가 포함되어 있으므로 O
"before"	: b가 포함되어 있으므로 O
"dude"		: a,b,c 모두 포함되지 않으므로 X

- 하이픈 : 두 문자 사이의 범위
[a-zA-Z] 	: 알파벳 모두
[0-9]		: 숫자

^ : NOT 의미
[^0-9]		: 숫자 X

\d	: 숫자
\D	: 숫자 X
\s	: whitespace 문자와 매치 ex) 탭, 줄바꿈, 스페이스 등
\S	: whitespace 문자 X
\w	: 문자 + 숫자
\W	: 문자 + 숫자 X

Dot(.)

모든 문자와 매치

a.b ==> a와 b 사이의 모든 문자
ex) a0b a5b acb akb
"""
#	match()		첫 문자열의 정규식과 매치되는지 조사			: LIKE 문자열%
#	search()	문자열 전체를 검색하여 정규식과 매치되는지 조사	 : LIKE %문자열%		
#	findall()	정규식과 매치되는 모든 문자열을 리스트로 돌려준다
#	finditer()	정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다
import re
p = re.compile('[a-z]+')

m = p.match("python")		#	성립
print("성립") if m else print("불가")

m = p.match("3 python")		#	불가
print("성립") if m else print("불가")

m = p.search("python")		#	성립
print("성립") if m else print("불가")

m = p.search("3 python")	#	성립
print("성립") if m else print("불가")