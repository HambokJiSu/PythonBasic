#   map 활용
#   1차원 배열의 split 결과를 새로운 배열에 등록
print("{0:=^25}".format("MAP"))
arr1 = ["aa 11", "bb 222", "cc 3", "dd 44444"]

def ufn_rtn2(p):
    return p.split(" ")[1]

arr2 = list(map(ufn_rtn2, arr1))
print("arr2:",arr2) #   ['11', '222', '3', '44444']

arr3 = list(map(lambda i: i.split(" ")[1], arr1))   #   arr2와 동일
print("arr3:",arr3) #   ['11', '222', '3', '44444']

#   filter 활용
#   배열의 양수 값만 빼서 새로운 배열에 등록
print("{0:=^25}".format("FILTER"))
arr1 = [1, -3, -2, 5, 6]

def ufn_rtnPlus(p):
    return p > 0

arr2 = list(filter(ufn_rtnPlus, arr1))
print("arr2:",arr2) #   ['11', '222', '3', '44444']

arr3 = list(filter(lambda i: i > 0, arr1))          #   arr2와 동일
print("arr3:",arr3) #   ['11', '222', '3', '44444']

#   zip 활용
print("{0:=^25}".format("ZIP"))
#   letters가 True일 경우에는 양수, False일 경우에는 음수로 변환
numbers = [1, 2, 3]
letters = [True, False, False]
arrRst = []
for i, j in zip(numbers, letters):  #   동일 사이즈가 아닌 배열도 가능하지만 짧은 배열 기준으로 종결되니 주의
    rst = i * (1 if j == True else -1)
    arrRst.append(rst)
print(arrRst)   #   [1, -2, -3]

print("="*20)
numbers = (1, 2, 3)
letters = ("A", "B", "C")
pairs = list(zip(numbers, letters))
print(pairs)    #   [(1, 'A'), (2, 'B'), (3, 'C')] 

arr1, arr2 = zip(*pairs)    #   unzip : zip 해제하기
print("arr1:",arr1)
print("arr2:",arr2)
print("="*20)

#   dict 만들기
keys = [1, 2, 3]
values = ["A", "B", "C"]
rst = dict(zip(keys, values))
print(rst)  #   {1: 'A', 2: 'B', 3: 'C'}

#   enumerate
#   for문에서 현재 위치의 인덱스가 필요할 때 유용
print("{0:=^25}".format("enumerate"))
arr1 = ['body', 'foo', 'bar']
for i, name in enumerate(arr1):
    print(i, name)  #   0 body, 1 foo, 2 bar