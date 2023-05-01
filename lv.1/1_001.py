'''
https://school.programmers.co.kr/learn/courses/30/lessons/64061
크레인 인형뽑기 게임

문제 설명
만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다. 
크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다. 
또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다. (그림에서는 화면표시 제약으로 5칸만으로 표현하였음)

게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때,
크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

[제한사항]
board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
0은 빈 칸을 나타냅니다.
1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
moves 배열의 크기는 1 이상 1,000 이하입니다.
moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.

'''


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
### 엘리사님 코드 실행 안되거나 이해 안되는 부분 있으면 말해주세요~! 이따 뵐게요 화이팅!!!