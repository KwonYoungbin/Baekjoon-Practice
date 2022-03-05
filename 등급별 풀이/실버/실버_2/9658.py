N = int(input())
dp = [0, 0, 1, 0, 1]

for i in range(5, N+1):
    if dp[i-1] == dp[i-3] == dp[i-4]:
        dp.append(0)
    else:
        dp.append(1)
        
print('SK' if dp[N] else 'CY')