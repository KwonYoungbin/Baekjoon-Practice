N = int(input())
dp = [0] * (N+1)
square = [i**2 for i in range(1, int(100000**(0.5))+1)]

for i in range(1, N+1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i-j])
    dp[i] = min(s) + 1
print(dp[N])