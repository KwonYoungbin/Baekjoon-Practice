# 이해 못함...

from collections import deque

moves = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(graph, n, m):
    q = deque([[0, 0, 1]])
    visited = [[[0]*2 for __ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    
    while q:
        x, y, w = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][w]
        
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and w == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])
    return -1

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
print(bfs(graph, n, m))
