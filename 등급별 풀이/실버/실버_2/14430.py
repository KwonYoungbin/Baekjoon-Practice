N, M = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(N)]

for x in range(N):
    for y in range(M):
        if x == y == 0:
            continue
        elif 1 <= x and 1 <= y:
            dp[x][y] += max(dp[x][y-1], dp[x-1][y])
        elif x == 0:
            dp[x][y] += dp[x][y-1]
        elif y == 0:
            dp[x][y] += dp[x-1][y]

print(dp[-1][-1])