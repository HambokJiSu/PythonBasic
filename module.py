#	shutil : 파일 복사
#	src => dst로 복사, 동일한 파일이 있을 경우 덮어씀
# import shutil
# shutil.copy("src.txt", "dst.txt")

#	glob : 디렉토리에 있는 파일들을 리스트로 만들기
import glob
list1 = glob.glob("./*.*")
print(list1)

import time
print(time.time())	#	현재 시간을 실수 형태로 돌려줌
print(time.strftime("%Y-%m-%d %H:%M:%S"))