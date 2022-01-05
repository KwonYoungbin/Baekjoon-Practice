import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0]*(n) for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(1, n):
    for start in range(n-i):
        end = start + i
        
        if arr[start] == arr[end]:
            if start+1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

print(*dp, sep='\n')
for i in range(int(sys.stdin.readline())):
    start, end = map(int ,sys.stdin.readline().split())
    print(dp[start-1][end-1])