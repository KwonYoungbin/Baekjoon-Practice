N = int(input())
tri = [0, 1]
adder = 1
counter = 2
while N > tri[-1]:
    adder += counter
    tri.append(tri[-1]+adder)
    counter += 1

dp = [int(1e9)] * (N+1)
dp[0], dp[1] = 0, 1

for i in range(2, N+1):
    if i in tri:
        dp[i] = 1
    else:
        for val in tri:
            if val > i:
                break
            dp[i] = min(dp[i], dp[i-val]+1)
print(dp[N])