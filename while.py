"""
타 프로그래밍 언어의
	continue
	break
동일
"""

treeHit = 0
while treeHit < 10:
	treeHit = treeHit + 1
	print(f"나무를 {treeHit}번 찍었습니다.")
	if treeHit == 10:
		print("나무 넘어갑니다.")