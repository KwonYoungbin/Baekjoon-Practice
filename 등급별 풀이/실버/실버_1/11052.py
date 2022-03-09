N = int(input())
cards = [0]+list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = cards[1]

for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+cards[j])
        
print(dp[N])