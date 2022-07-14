import numpy as np

"""
물건이 놓인 칸 : -1
물건이 없이 먼지가 쌓인칸 : 0이상의 정수

go : 현재 바라보는 방향으로 한 칸 전진, 격자를 벗어나거나 물건이 놓였있으면 다음 명령 수행
left : 바라보는 방향을 왼쪽으로 회전
right : 바라보는 방향을 오른쪽으로 회전

먼지가 0인 칸도 청소하지만 청소하는 먼지의 양은 0

청소한 먼지의 양을 최종 return

청소기는 시작 시 북쪽을 바라보고 시작
"""
def solution(office, r, c, move):
	npOffice = np.array(office)

	rtnList = []
	rtnAmt = 0

	#	0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
	direction = 0

	rtnList.append(rtnCleanAmt(npOffice, r, c))
	npOffice[r, c] = 0

	new_c = -1	#	X축
	new_r = -1	#	Y축

	for i in move:

		print("*"*20)
		print("move:",i)
		print("direction:",str(direction))
		print("c:",str(c))
		print("r:",str(r))

		new_c = c
		new_r = r

		#	진행 방향에 물건이 있거나 더이상 진행할 수 없을 경우 좌표를 수정하지 않는다.
		if i == "go":
			if direction == 0 :	# 북쪽
				if new_r - 1 < 0 :
					continue
				else:
					new_r = r - 1
			elif direction == 1 :	# 동쪽
				if new_c + 1 > len(office) - 1 :
					continue
				else:
					new_c = c + 1
			elif direction == 2 :	# 남쪽
				if new_r + 1 > len(office) - 1 :
					continue
				else:
					new_r = r + 1
			elif direction == 3 :	# 서쪽
				if new_c - 1 < 0 :
					continue
				else:
					new_c = c - 1

			print("new_c:",new_c)
			print("new_r:",new_r)
			rtnAmt = rtnCleanAmt(npOffice, new_r, new_c)

			if rtnAmt == -1:
				continue

			npOffice[new_r, new_c] = 0
			rtnList.append(rtnAmt)
			r = new_r
			c = new_c
			# print("r:",r)
			# print("c:",c)
		else:
			direction = rtnCurDir(direction, i)
			# print("direction:",str(direction))
	
	# print("rtnList:",rtnList)
	answer = np.array(rtnList).sum()
	return int(answer)

def rtnCurDir(direction, move):
	# print("rtnCurDir")
	# print("direction:",direction)
	# print("move:",move)
	if move == "right":
		direction = direction + 1 if direction + 1 <= 3 else 0
	else:	#	left
		direction = direction - 1 if direction - 1 >= 0 else 3

	return direction

def rtnCleanAmt(npOffice, r, c):
	cleanAmt = 0

	print("rtnCleanAmt:", npOffice[r,c])

	cleanAmt = -1 if npOffice[r,c] == -1 else npOffice[r,c]

	return cleanAmt	# 정상적인 이동이 실패했을 경우 -1 리턴


list1 = [[5,-1,4],[6,3,-1],[2,-1,1]]
#list1 = [[5,-1],[5,-1]]
r = 1
c = 0
move = ["go","go","right","go","right","go","left","go"]
#move = ["go","left","left","left","left","left","left","left","left","left","left","left","go","go","go","go","go","go","go","go","go","left","go","right","right","go","go"]
# move = ["go","right","right","right","right","right","right","right","right","right","right","right","right","right","right","right","right","right","right","right","right"]
# move = ["go"]
rtn = solution(list1, r, c, move)
print("최종:",rtn)