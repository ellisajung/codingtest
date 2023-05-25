"""
https://school.programmers.co.kr/learn/courses/30/lessons/42862
체육복

문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 
다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
학생들의 번호는 체격 순으로 매겨져 있어, 
바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 
최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
"""

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
# return = 5


# 네비게이터
# 체육복 있음 : 1, 없음 : 0
# 학생 전체 수를 리스트로 나타내기 : [1 for _ in range(n)]
# 학생의 체육복 현황을 체크해주기 for문으로 lost에 속한 index들을 0로 바꾸면 될듯
# 예제 1의 경우 : [1, 0, 1, 0, 1]
# reserve에 속한 index 양옆 값을 검증해if서 둘 중 하나를 1로 바꿔줘
# count 메소드로 리스트 전체의 1 개수를 세줘


# 학생 전체 수를 리스트로 나타내기
students = [1 for _ in range(n)]
print(students)

# 학생의 체육복 현황을 체크해주기 for문으로 lost에 속한 index들을 0로 바꾸면 될듯
for i in lost:
    students[i - 1] = 0
print(students)

# reserve에 속한 index 양옆 값을 검증해서 둘 중 하나를 1로 바꿔줘
for j in reserve:
    if j not in lost:
        if j - 2 >= 0 and students[j - 2] == 0:
            students[j - 2] = 1
            continue

        if j < n and students[j] == 0:
            students[j] = 1
            continue
    students[j] = 1

print(students)

# count 메소드로 리스트 전체의 1 개수를 세줘
print(sum(students))

# def solution(n, lost, reserve):
#     students = [1 for _ in range(n)]
#     for i in lost:
#         students[i - 1] = 0
#     for j in reserve:
#         if j - 2 >= 0 and students[j - 2] == 0:
#             students[j - 2] = 1
#             continue
#         if j < n and students[j] == 0:
#             students[j] = 1
#     return sum(students)


def solution(n, lost, reserve):
    if j not in lost:
        if j - 2 >= 0 and students[j - 2] == 0:
            students[j - 2] = 1
        elif j < n and students[j] == 0:
            students[j] = 1
    else:
        students[j - 1] = 1
    return sum(students)


def solution(n, lost, reserve):
    students = [1 for _ in range(n)]
    for i in lost:
        students[i - 1] = 0
    for j in reserve:
        if students[j - 1] == 1:
            if j - 2 >= 0 and students[j - 2] == 0:
                students[j - 2] = 1
            elif j < n and students[j] == 0:
                students[j] = 1
        else:
            students[j - 1] = 1
    return sum(students)


def solution(n, lost, reserve):
    students = [1 for _ in range(n)]

    for i in lost:
        students[i - 1] -= 1
    for i in reserve:
        students[i - 1] += 1

    for i in range(n):
        if students[i] == 0:
            if i > 0 and students[i - 1] == 2:
                students[i - 1] -= 1
                students[i] += 1
            elif i < n - 1 and students[i + 1] == 2:
                students[i + 1] -= 1
                students[i] += 1

    return n - students.count(0)
