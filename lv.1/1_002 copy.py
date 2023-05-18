'''
https://school.programmers.co.kr/learn/courses/30/lessons/132267
콜라 문제

문제 설명
문제를 열심히 풀던 상빈이는 일반화된 콜라 문제를 생각했습니다. 
이 문제는 빈 병 a개를 가져다주면 콜라 b병을 주는 마트가 있을 때, 
빈 병 n개를 가져다주면 몇 병을 받을 수 있는지 계산하는 문제입니다. 
기존 콜라 문제와 마찬가지로, 보유 중인 빈 병이 a개 미만이면, 
추가적으로 빈 병을 받을 순 없습니다. 상빈이는 열심히 고심했지만, 
일반화된 콜라 문제의 답을 찾을 수 없었습니다. 상빈이를 도와, 
일반화된 콜라 문제를 해결하는 프로그램을 만들어 주세요.

콜라를 받기 위해 마트에 주어야 하는 병 수 a, 
빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수 b, 
상빈이가 가지고 있는 빈 병의 개수 n이 매개변수로 주어집니다. 
상빈이가 받을 수 있는 콜라의 병 수를 return 하도록 
solution 함수를 작성해주세요.

제한사항
1 ≤ b < a ≤ n ≤ 1,000,000
정답은 항상 int 범위를 넘지 않게 주어집니다.
'''


a = 2
b = 1
n = 20
# result = 19

answer = 0
while n>=a:
    answer += (n//a)*b
    n = (n//a)*b + n%a
    # print (answer)



# 수학적 일반화로 풀기
def solution(a, b, n):
    k = int((n-a)/(a-b)) + 1
    answer = k*b
    return answer

# 반복문으로 풀기
def solution2(a, b, n):
    answer = 0
    while n>=a:
        answer += (n//a)*b
        n = (n//a)*b + n%a
    return answer

# 재귀함수
def coke(a,b,n,answer=0):
    if n < a: return answer
    return coke(a,b, (n//a)*b + n%a, answer+(n//a)*b)
print(coke(a,b,n))


