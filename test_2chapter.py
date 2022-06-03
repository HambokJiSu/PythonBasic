#	2장 연습문제

#	Q1
dic1 = {"국어":80, "영어":75, "수학":55}
list1 = dic1.values()
iSum = 0
for i in list1:
	iSum += i

print(iSum/len(list1))

#	Q2
i1 = 13
if i1 % 2 == 1:
	print("홀수")
else:
	print("짝수")

#	Q3
str1 = "881120-1068234"
print(str1[:6])
print(str1[7:])

#	Q4
str1 = "881120-1068234"
print(str1[7])

#	Q5
str1 = "a:b:c:d"
print(str1.replace(":", "#"))

#	Q6
list1 = [1,3,5,4,2]
list1.sort()
list1.reverse()
print(list1)

#	Q7
list1 = ["Life", "is", "too", "short"]
print(" ".join(list1))

#	Q8
t1 = (1,2,3)
t2 = (4,)
t1 = t1 + t2
print(t1)

#	Q9 : dictionary Type에 List는 추가할 수 없다?
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
#a[[1]] = ['python']
a[250] = 'python'
print(a)

#	Q10
a = {"A":90, "B":80, "C":70}
print(a.get("B"))

#	Q11
a = [1,1,1,2,2,3,3,3,4,4,5]
set1 = set(a[:])
print(set1)

#	Q12 : 동일한 주소값을 바라봄. 분리를 위해서는 별도 복사를 수행해야함
a = b = [1,2,3]
a[1] = 4
print(b)