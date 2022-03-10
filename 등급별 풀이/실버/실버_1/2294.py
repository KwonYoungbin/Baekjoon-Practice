N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
dp = [int(1e9)] * (K+1)
dp[0] = 0

for money in arr:
    for i in range(money, K+1):
        dp[i] = min(dp[i], dp[i-money]+1)
        
print(dp[K] if dp[K] != int(1e9) else -1)