from collections import deque

moves = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def bfs(a, b):
    q = deque([(0,(a, b))])
    visited = [[False]*M for _ in range(N)]
    visited[a][b] = True
    
    while q:
        dist, pos = q.popleft()
        x, y = pos
        
        if graph[x][y] == 1:
            return dist
        
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((dist+1, (nx, ny)))
    return max(N, M)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0

for x in range(N):
    for y in range(M):
        if not graph[x][y]:
            result = max(result, bfs(x, y))
print(result)