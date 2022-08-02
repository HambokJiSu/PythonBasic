"""
import itertools
"""
from itertools import combinations

def solution(nums):
    n_div2 = len(nums) / 2
    arrSet = set(nums)
    
    print("n_div2:",n_div2)
    print("arrSet:",arrSet)
    answer = n_div2 if len(arrSet) > n_div2 else len(arrSet)
    return int(answer)

rst = solution([3,3,3,2,2,2])
print(rst)