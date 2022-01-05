# 연쇄 행렬 최소 곱셈 대표 문제(기억할 것) 
# 단, Python3 에서는 시간초과가 나기 때문에, PyPy3에서 할 것.
# 다른 알고리즘이 있는지 확인해볼 필요가 있음.

INF = int(1e9)

n = int(input())
arr = list(map(int,input().split()))

for _ in range(n-1):
    l, r = map(int, input().split())
    arr.append(r)

dp = [[0]*n for _ in range(n)]

for d in range(1, n):
    for i in range(n-d):
        j = i+d
        
        dp[i][j] = INF
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i]*arr[k+1]*arr[j+1])

print(dp[0][-1])