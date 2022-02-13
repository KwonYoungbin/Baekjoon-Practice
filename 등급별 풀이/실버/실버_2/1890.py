N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if x == y == N-1:
            break
        jump = graph[x][y]
        if y + jump < N:
            dp[x][y+jump] += dp[x][y]
        if x + jump < N:
            dp[x+jump][y] += dp[x][y]

print(dp[-1][-1])