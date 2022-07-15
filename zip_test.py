"""
zip  문법
"""
numbers = [1, 2, 3]
letters = [True, False, False]
for i, j in zip(numbers, letters):
    rst = i * (1 if j == True else -1)
    print(rst)

print("="*20)
numbers = (1, 2, 3)
letters = ("A", "B", "C")
pairs = list(zip(numbers, letters))
print(pairs)
#   [(1, 'A'), (2, 'B'), (3, 'C')] 

arr1, arr2 = zip(*pairs)    #   unzip
print("arr1:",arr1)
print("arr2:",arr2)
print("="*20)
#   dict 만들기
keys = [1, 2, 3]
values = ["A", "B", "C"]
rst = dict(zip(keys, values))
print(rst)
#   {1: 'A', 2: 'B', 3: 'C'}