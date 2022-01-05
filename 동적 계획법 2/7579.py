# 냅색을 응용한 문제로, 점화식을 잘 세우는 방법을 공부해야 함.

INF = int(1e9)

n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
dp = [[0]*(sum(costs)+1) for _ in range(n+1)]

result = INF

for i in range(n):
    byte = memories[i]
    cost = costs[i]
    
    for j in range(sum(costs)+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])
        
        if dp[i][j] >= m:
            result = min(result, j)
print(result)