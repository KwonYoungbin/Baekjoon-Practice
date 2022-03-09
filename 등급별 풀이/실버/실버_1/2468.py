from collections import deque

moves = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(a, b, visited, standard):
    q = deque([(a, b)])
    visited[a][b] = True
    
    while q:
        x, y = q.popleft()
        
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] >= standard:
                q.append((nx, ny))
                visited[nx][ny] = True
    

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0
min_val = min(map(min, graph))
max_val = max(map(max, graph))

for i in range(min_val, max_val+1):
    visited = [[False]*N for _ in range(N)]
    count = 0
    for x in range(N):
        for y in range(N):
            if graph[x][y] >= i and not visited[x][y]:
                bfs(x, y, visited, i)
                count += 1
    if count > result:
        result = count
        
print(result)