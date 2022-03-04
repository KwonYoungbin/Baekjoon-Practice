from collections import deque

moves = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(a, b):
    global sheep, wolf
    
    q = deque([(a, b)])
    visited[a][b] = True
    o_cnt = 0
    v_cnt = 0
    
    while q:
        x, y = q.popleft()
        
        if graph[x][y] == 'v':
            v_cnt += 1
        elif graph[x][y] == 'o':
            o_cnt += 1
            
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                
    if o_cnt > v_cnt:
        sheep += o_cnt
    else:
        wolf += v_cnt

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
sheep = 0
wolf = 0

for x in range(R):
    for y in range(C):
        if graph[x][y] != '#' and not visited[x][y]:
            bfs(x, y)
print(sheep, wolf)