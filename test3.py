import numpy as np

def solution(r, c):
	
	nArray = np.zeros((r,c))
	print(nArray)
	# mapp = [[0] * (r+1) for _ in range(c+1)]
	# print(mapp)
    
	# mapp[1][1] = 1
    
	# for i in range(1, c+1):
	# 	for j in range(1, r+1):
	# 		if i == 1 and j == 1:
	# 			continue

	# 		mapp[i][j] = mapp[i-1][j] + mapp[i][j-1]
	# 		print("i:",i,"j:",j)
	# 		print(mapp[i-1][j] + mapp[i][j-1])

	# return mapp[-1][-1]	

rtn = solution(2, 4)
print(rtn)