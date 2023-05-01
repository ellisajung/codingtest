'''
https://school.programmers.co.kr/learn/courses/30/lessons/181945
문자열 돌리기

문제 설명
문자열 str이 주어집니다.
문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

제한사항
1 ≤ str의 길이 ≤ 10

'''

# str = abcde
# # result
# # a
# # b
# # c
# # d
# # e

# str = input()
# for s in str:
#     print(s)

# str = input()
# print("\n".join(list(str)))





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