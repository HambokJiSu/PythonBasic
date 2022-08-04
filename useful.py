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

#   리스트의 모든 조합 구하기
print("{0:=^25}".format("itertools"))
import itertools

arr1 = [1, 2, 3]
#   permutations(array, n) : array에 대해 n개에 대한 조합 (순서 상관)
rst = list(itertools.permutations(arr1, 2))
print(rst)  #   [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

#   combinations(array, n) : array에 대해 n개에 대한 조합 (순서 무관)
rst = list(itertools.combinations(arr1, 2))
print(rst)  #   [(1, 2), (1, 3), (2, 3)]

print("{0:=^25}".format("join : 리스트 문자열 합치기"))

list1 = ["1", "3", "5", "6", "7", "9"]
print("".join(list1))
print("-".join(list1))  #   공백 이외의 문자 입력 시 리스트 사이에 해당 문자 출력

list2 = [1, 3, 5, 6, 7, 9]
#   리스트 내용이 문자열이 아니면 오류 발생!!!!
#   map 활용하여 문자열로 변환 후 처리하자
list2 = list(map(lambda i:str(i), list2))
print("".join(list2))

print("{0:=^25}".format("리스트 내포"))

list1 = [1,2,3,4,5,6]
list2 = [5,6,7,8,9]

_list1 = [i for i in list1 if i not in list2]
_list2 = [i for i in list2 if i not in list1]

print(_list1)
print(_list2)

list3 = [i for i in range(1, 10)]
print(list3)

list4 = [i + j for i in range(1, 10) if i % 3 == 0 for j in range(1, 10) if j % 2 == 0]
print(list4)

print("{0:=^25}".format("n진법 변환"))

def convert_iter(num, base):
    
    tmp = ''
    while num:
        tmp = str(num%base) + tmp
        num //= base
    return tmp

rst = convert_iter(10, 3)	#	10진법 to 3진법
print(rst)

rst2 = int(rst, 3)			#	3진법 to 10진법
print(rst2)

print("{0:=^25}".format("소수(Prime Number) 구하기"))

from math import sqrt
def primenumber(x):
	for i in range(2, int(sqrt(x) + 1)):   # 2부터 x의 제곱근까지의 숫자
		if x % i == 0:  # 나눠떨어지는 숫자가 있으면 소수가 아님
			return False
	return True

print(primenumber(7))
print(primenumber(10))
print(primenumber(12))
print(primenumber(13))