"""
크레인 인형뽑기 게임

크레인을 모두 작동시켜서 터트려져 사라진 인형의 개수 리턴

ex)
[   
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]
[1,5,3,5,1,2,1,4]

주안점)
 - board 배열의 숫자는 인형의 종류를 의미, 0은 인형이 없음을 의미함
 - move 배열은 1이상, board 배열의 가로크기 이하의 자연수
 - 뽑은 인형을 쌓는 공간에는 스택형태로 저장됨
 - 뽑은 인형이 연속해서 동일한 인형이면 터트려져 사라짐
 - 뽑은 인형은 무한히 쌓을 수 있다는 가정

 - board 배열은 뽑아가면 0으로 수정해야함
 - stack 배열에도 터트려지면 2개는 같이 사라짐
"""

def solution(board, moves):

    listGet = []    #   뽑은 바구니

    dollNum = 0
    answer = 0
    for i in moves:
        for j in range(len(board)):
            print("i:%d,j:%d" % (i, j))
            print(board[j][i-1])
            if board[j][i-1] > 0:
                dollNum = board[j][i-1]
                board[j][i-1] = 0

                if len(listGet) > 0 and listGet[-1] == dollNum:
                    listGet.pop()
                    answer += 2
                else:
                    listGet.append(dollNum)

                print("listGet:",listGet)
                
                break

    return answer

rst = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	)
print(rst)