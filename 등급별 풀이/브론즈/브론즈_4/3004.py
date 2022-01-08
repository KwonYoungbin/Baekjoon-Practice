n = int(input())
dp = [0,2]
for i in range(2, n+1):
    dp.append(dp[-1]+(i//2)+1)
print(dp[n])