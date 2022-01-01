n = int(input())
dp = [0] * (n+1)

if n == 0:
    print(0)
else:
    for i in range(2, n+1):
        dp[i] = dp[i-1]+1
        
        if i%2 == 0 and dp[i] > dp[i//2] + 1:
            dp[i] = dp[i//2] + 1
        
        if i%3 == 0 and dp[i] > dp[i//3] + 1:
            dp[i] = dp[i//3] + 1
print(dp[n])