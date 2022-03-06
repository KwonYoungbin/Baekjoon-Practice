N = int(input())
cards = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if cards[i] > cards[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))