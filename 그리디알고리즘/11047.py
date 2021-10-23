import sys

n, k = map(int,sys.stdin.readline().split())
money = []
answer = 0

for _ in range(n):
    money.append(int(sys.stdin.readline()))

while k != 0:
    answer += k//money[n-1]
    k %= money[n-1]
    n -= 1
    
print(answer)