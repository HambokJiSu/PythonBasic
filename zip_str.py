#	문자열 압축 알고리즘
def solution(s):

	result = list()
	
    #	문자열 사이즈만큼 반복
	for i in range(1, len(s) + 1):
		result.append(str_zip(s, i))

	# print("solution print")
	# print(result)
	result.sort()
	answer = result[0]
	return answer

#	해당 사이즈가 반환하는 총 문자열 사이즈 반환
def str_zip(s, size):

	prevStr = ""
	resultStr = ""

	dupCnt = 1
	
	import math
	loopCnt = math.ceil(len(s) / size)
	currInx = 0
	i = 0

	# for i in range(0, len(s), size):
	while currInx <= loopCnt:
		# print("##", str(i), "##")
		# if prevStr == "":
		# 	prevStr = s[0:size]
		# 	# print("if1 prevStr :",prevStr)
		# 	currInx += 1
		# 	i = currInx * size
		# 	continue

		if prevStr == s[i:i+size]:
			# print("if2 prevStr :",prevStr)
			# print("if2 s[i:i+size-1] :",s[i:i+size])
			dupCnt += 1
		else:
			# print("if3 prevStr :",prevStr)
			# print("if3 s[i:i+size-1] :",s[i:i+size])
			resultStr += ( str(dupCnt) if dupCnt > 1 else "" ) + prevStr
			prevStr = s[i:i+size]
			dupCnt = 1

		if currInx == loopCnt:
			resultStr += ( str(dupCnt) if dupCnt > 1 else "" ) + prevStr
			prevStr = s[i:i+size]

		currInx += 1
		i = currInx * size

	# print(str(size), ":", resultStr)

	return len(resultStr)

if __name__ == '__main__':
	#str_zip("aabbaccc", 9)
	#print(solution("aabbaccc"))			#	2a2ba3c
	#print(solution("ababcdcdababcdcd"))
	#print(solution("abcabcdede"))
	print(solution("abcabcabcabcdededededede"))
	#print(solution("xababcdcdababcdcd"))