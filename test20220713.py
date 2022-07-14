def solution(record):

	answer = []
	arr2 = []

	#	id, nm Dictionary를 만들고 관리한 후 최종 메시지에 적용해야 함
	dictIdNm = {}
	# del dictIdNm[""]

	for i in record:
		arrItem = i.split(" ")
		if arrItem[0] != "Leave":
			dictIdNm[arrItem[1]] = arrItem[2]
			
		if arrItem[0] != "Change":
			arr2.append(arrItem)

	for i in arr2:
		answer.append(rtnMsg(i[0], i[1], dictIdNm))
    
	return answer

def rtnMsg(tp, id, dictIdNm):
    return "%s님이 %s습니다." % (dictIdNm.get(id), "들어왔" if tp == "Enter" else "나갔")

list1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
rtn = solution(list1)
print(rtn)