from collections import deque

moves = [(1,0), (0,1), (-1,0), (0,-1)]

def bfs(a, b):
    q = deque([(a, b)])
    graph[a][b] = 2
    
    while q:
        x, y = q.popleft()
        
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))

M, N = map(int, input().split())
graph = [list(map(int, input())) for _ in range(M)]

for y in range(N):
    if graph[0][y] == 0:
        bfs(0, y)
        
print('YES' if 2 in graph[-1] else 'NO')