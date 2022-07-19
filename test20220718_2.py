"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

입출력 예
nums	    result
[1,2,3,4]	1
[1,2,7,6,4]	4

입출력 예 #1
[1,2,4]를 이용해서 7을 만들 수 있습니다.

입출력 예 #2
[1,2,4]를 이용해서 7을 만들 수 있습니다.
[1,4,6]을 이용해서 11을 만들 수 있습니다.
[2,4,7]을 이용해서 13을 만들 수 있습니다.
[4,6,7]을 이용해서 17을 만들 수 있습니다.

조건
 - 3개의 수를 일단 더한 다음 소수가 있는지 확인
 - 3개 조합의 파라미터를 어떻게 던질 수 있을지?
"""
import math
from itertools import combinations

def solution(nums):
    answer = 0
    nList = list(combinations(nums, 3))
    #print(nList)
    for i in nList:
        answer += 1 if bUniqueNum(sum(i)) else 0
    
    return answer

#   소수 여부 리턴
def bUniqueNum(num):
    # for i in range(2, num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False
    
    return True

#rst = solution([1,2,3])
#rst = solution([1,2,3,4])
rst = solution([1,2,7,6,4])
#rst = bUniqueNum(17)
print(rst)