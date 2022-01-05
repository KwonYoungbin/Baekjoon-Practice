# 자주 나오는 문제인 듯하니 기억할 것.

n, k = map(int, input().split())
moneys = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1

for m in moneys:
    for i in range(m, k+1):
        dp[i] += dp[i-m]
print(dp[k])