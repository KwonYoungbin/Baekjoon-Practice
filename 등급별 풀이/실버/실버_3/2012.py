import sys
input = sys.stdin.readline

n = int(input())
rank = [0] + [int(input()) for _ in range(n)]
rank.sort()
result = 0

for i in range(1, n+1):
    result += abs(rank[i]-i)
print(result)