N = int(input())
health = list(map(int, input().split()))
pleasure = list(map(int, input().split()))

dp = [[0]*100 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(100):
        if j < health[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-health[i-1]]+pleasure[i-1])

print(dp[-1][-1])