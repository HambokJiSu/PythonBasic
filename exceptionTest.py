try:
	raise FileExistsError
	4/0
	a = [1,3]
	print(a[3])
# except:
# 	print("모든 오류")
# except (ZeroDivisionError, IndexError) as e:
# 	print(f"오류 묶어서 처리 : {e}")
except ZeroDivisionError as e:
	print(f"Exception : {e}")
except IndexError as e:
	print(f"Exception : {e}")
except FileExistsError as e:
	pass	# 오류 건너뛰기
finally:
	print("여긴 마지막에 수행")