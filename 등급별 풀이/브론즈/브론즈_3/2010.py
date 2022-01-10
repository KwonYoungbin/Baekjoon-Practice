import sys
input = sys.stdin.readline

n = int(input())
result = 0
for _ in range(n):
    result += int(input())
print(result-n+1)