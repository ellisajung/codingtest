'''
https://school.programmers.co.kr/learn/courses/30/lessons/64061
크레인 인형뽑기 게임

문제 설명
해당 코드는 인형뽑기 게임에서 인형을 뽑는 과정을 시뮬레이션하고, 
제거된 인형의 개수를 반환

제한사항
board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
0은 빈 칸을 나타냅니다.
1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
moves 배열의 크기는 1 이상 1,000 이하입니다.
moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.

'''

# 지인님 풀이

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
# result = 4

# basket = [4, 3, 1, 1, 3, 2, 0, 4]
##############################################
# 한번 없애면: [4, 3, 3, 2, 0, 4]  # answer = 2
# 두번 없애면: [4, 2, 0, 4]  # answer = 4
##############################################
# 아니면 basket 만들 때 같은 것 check

# def solution(board, moves):
#     answer = 0
#     check = 0
#     for i in board:
#         for j in moves:
#             if i[j-1] != 0:
#                 if i[j-1] == check:
#                     answer += 2
#                 print(check)
#                 check = i[j-1]
#             i[j-1] = 0
#     return answer


def solution(board, moves):
    answer = 0
    basket = [0]  # board에서 0은 빈칸. basket에 0 append 안됨.
    for j in moves:
        for i in board:  #  moves[0]인 1을 기준으로 i[1-1]=i[0]들을 체크하고 싶은거니까 for문 순서 바꾸기 

            if i[j-1] != 0:
                if i[j-1] == basket[-1]:  # basket에 새로 들어올 값이랑 현재 basket의 맨 마지막 값이랑 같으면
                    answer += 2
                    basket.pop()  # basket에서 맨 마지막꺼 빼기
                else:
                    basket.append(i[j-1])
                i[j-1] = 0  # 빈칸으로 만들어주기
                break  # 모든 i들을 다 하는게 아니라 0이 아닌 값을 찾으면 for문 빠져나오게!
            else:
                pass  # 세로줄에 0만 있으면 아무 동작 안하게
    return answer

print(solution(board, moves))




# 내풀이(정답 참고)

board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]] # 인형뽑기 게임판의 상태
moves = [1,5,3,5,1,2,1,4] # 인형 뽑는 위치
# result = 4

def solution(board, moves):
    basket = [] # 인형을 넣을 빈 리스트
    answer = 0 # 제거된 인형의 개수 초기화

    for i in moves: # moves 리스트의 원소를 하나씩 도는데,
        for j in range(len(board)): # 이 때 board 리스트의 원소를 돌면서,
            if board[j][i-1] != 0: # 해당 위치에서 가장 위에 있는 인형을 뽑아준다.
                basket.append(board[j][i-1])
                board[j][i-1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop(-1)
                        basket.pop(-1)
                        answer += 2     
                break
    return answer