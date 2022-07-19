def solution(absolutes, signs):

    arrRst = []
    for i, j in zip(absolutes, signs): 
        arrRst.append(i * (1 if j else -1))

    return sum(arrRst)

rst = solution([4,7,12], [True,False,True])
print(rst)