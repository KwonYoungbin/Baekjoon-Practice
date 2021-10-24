import sys

#팩토리얼의 5 개수 세는 함수
def five_count(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

#팩토리얼의 2 개수 세는 함수
def two_count(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer

n, m = map(int, sys.stdin.readline().split())

if m == 0:
    print(0)
else:
    print(min(two_count(n)-two_count(m)-two_count(n-m), five_count(n)-five_count(m)-five_count(n-m)))