import sys
sys.setrecursionlimit(10**6)

moves = [(0,1), (0,-1), (1,0), (-1,0)]

def dfs(graph, x, y, m, n, dp):
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for move in moves:
        nx = x + move[0]
        ny = y + move[1]
        if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(graph, nx, ny, m, n, dp)
    return dp[x][y]
    

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
dp[m-1][n-1] = 1

print(dfs(graph, 0, 0, m, n, dp))