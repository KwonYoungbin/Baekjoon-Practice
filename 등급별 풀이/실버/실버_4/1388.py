from collections import deque

row_moves = [(1, 0), (-1, 0)]
col_moves = [(0, 1), (0, -1)]
N, M = map(int, input().split())
graph = [input() for _ in range(N)]

def bfs(graph, visited, a, b):
    q = deque([(a, b)])
    visited[a][b] = True
    
    if graph[a][b] == '-':
        while q:
            x, y = q.popleft()
            
            for move in col_moves:
                nx = x + move[0]
                ny = y + move[1]
                
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == '-' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    else:
        while q:
            x, y = q.popleft()
            
            for move in row_moves:
                nx = x + move[0]
                ny = y + move[1]
                
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == '|' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
        
                
result = 0
visited = [[False]*M for _ in range(N)]

for x in range(N):
    for y in range(M):
        if not visited[x][y]:
            bfs(graph, visited, x, y)
            result += 1
print(result)