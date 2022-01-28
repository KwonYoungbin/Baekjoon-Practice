import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = 0

for _ in range(n):
    now = list(map(int, input().strip().split()))
    if now[0] == 0:
        if stack:
            stack[-1][1] -= 1
    else:
        stack.append([now[1], now[2]-1])
    
    if stack and stack[-1][1] == 0:
        score, time = stack.pop()
        result += score

print(result)