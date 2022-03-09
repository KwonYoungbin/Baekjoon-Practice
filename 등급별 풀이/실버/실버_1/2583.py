from collections import deque

moves = [(1,0),(-1,0),(0,-1),(0,1)]

def bfs(a, b):
    global result
    q = deque([(a, b)])
    graph[a][b] = 2
    count = 1
    while q:
        x, y = q.popleft()
        
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 2
                count += 1
    
    result.append(count)

M, N, K = map(int, input().split())
graph = [[1]*N for _ in range(M)]
result = []

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    
    for x in range(lx, rx):
        for y in range(ly, ry):
            graph[y][x] = 0
    
for x in range(M):
    for y in range(N):
        if graph[x][y] == 1:
            bfs(x,y)

result.sort()
print(len(result))
print(*result)