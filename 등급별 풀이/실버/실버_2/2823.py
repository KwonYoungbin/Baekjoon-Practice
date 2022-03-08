from collections import deque

moves = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(a, b):
    q = deque([(a, b)])
    
    while q:
        x, y = q.popleft()
        count  = 0
        
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.':
                count += 1
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
        if count < 2:
            return 1
    return 0

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]

flag = False

for x in range(R):
    for y in range(C):
        if graph[x][y] == '.':
            print(bfs(x, y))
            flag = True
            break
        
    if flag == True:
        break