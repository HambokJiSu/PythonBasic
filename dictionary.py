dic = {'name':'chan','age':41}
print(dic)
dic[3] = 'test'	#	추가
print(dic)
del dic[3]		#	삭제

print(dic.keys())	#	키 값 목록 추출
print(list(dic.keys()))	#	키 값 목록 리스트로 변환

print(dic.values())	#	값 목록 추출
print(list(dic.values()))	#	값 목록 리스트로 변환

print(dic['age'])	#	값 추출 정상
#print(dic['age2'])	#	미존재 값 추출 : 오류 발생
print(dic.get('age'))	# 값 추출 정상
print(dic.get('age2'))	# 미존재 값 추출 : None 반환
print(dic.get('age2', '없어'))	# 미존재 값 추출 시 기본값 지정

print('age' in dic)	#	값 존재여부 확인 : True
print('age2' in dic)	#	값 존재여부 확인 : False