import numpy as np

def solution(office, k):

	#print(office)

	npOffice = np.array(office)
	#print(npOffice)

	rtnList = []
	for i in np.arange(0, len(office)):
		for j in np.arange(0, len(office)):
			rtnList.append(rtnHit(npOffice, k, i, j))

	rtnList.sort()
	rtnList.reverse()

	return rtnList[0]

def rtnHit(npOffice, k, x, y):
	limitX = len(npOffice) if x + k > len(npOffice)  else x + k
	limitY = len(npOffice) if y + k > len(npOffice) else y + k
	print("x:",x,"limitX:", limitX)
	print("y:",y,"limitY:", limitY)

	targetOffice = npOffice[x:limitX, y:limitY]
	print(targetOffice)
	targetOffice = np.concatenate(targetOffice).tolist()
	
	return targetOffice.count(1)

list1 = [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,1,0]]
list1 = [[1,0,0],[0,0,1],[1,0,0]]
rtn = solution(list1, 2)
print(rtn)