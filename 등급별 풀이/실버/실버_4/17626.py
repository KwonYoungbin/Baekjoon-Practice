import math

n = int(input())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = 1 if i == int(math.sqrt(i))**2 else i
        

for i in range(2, n+1):
    for j in range(1, int(math.sqrt(i))+1):
        root = j**2
        dp[i] = min(dp[i], dp[root] + dp[i - root])
        
print(dp[n])