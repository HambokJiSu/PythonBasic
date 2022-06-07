"""
3과 5의 배수 합하기
"""
def getSum3or5(pLastNum):
	iSum = 0
	for i in range(1, pLastNum + 1):
		if(i % 3 == 0 or i % 5 == 0):
			iSum += i

	print(iSum)

if(__name__ == "__main__"):
	getSum3or5(1000)