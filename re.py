#   정규식 테스트
import re

s = "어쩌구저쩌구가"
#p = re.compile(".*을|.*를|.*은|.*는|.*이|.*가")
p = re.compile(".*을$|.*를$|.*은$|.*는$|.*이$|.*가$")
r = p.search(s)
if r != None : s = s[:-1]
print(s)

#print(r)