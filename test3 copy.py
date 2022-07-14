import numpy as np

def solution(r, c):
	
	nArray = [[0] * (r+1) for _ in range(c+1)]
	#print(nArray)
    
	nArray[1][1] = 1
    
	for i in range(1, c+1):
		for j in range(1, r+1):
			if i == 1 and j == 1:
				continue

			nArray[i][j] = nArray[i-1][j] + nArray[i][j-1]

	return nArray[-1][-1]	

rtn = solution(2, 4)
print(rtn)