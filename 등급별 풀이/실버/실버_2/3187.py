from collections import deque

moves = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(a, b):
    global sheep, wolf
    s, w = 0, 0
    q = deque([(a, b)])
    visited[a][b] = True
    
    while q:
        x, y = q.popleft()
        
        if graph[x][y] == 'v':
            w += 1
        elif graph[x][y] == 'k':
            s += 1
        
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

    if s > w:
        sheep += s
    else:
        wolf += w

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
sheep, wolf = 0, 0

for x in range(R):
    for y in range(C):
        if graph[x][y] != '#' and not visited[x][y]:
            bfs(x, y)
print(sheep, wolf)