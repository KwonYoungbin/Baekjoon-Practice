from collections import deque

t = int(input())
moves = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(graph, x, y, m, n, visited):
    q = deque([[x,y]])
    visited[y][x] = True
    while q:
        now_x, now_y = q.popleft()
        
        for move in moves:
            nx = now_x + move[0]
            ny = now_y + move[1]
            
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == 1:
                q.append([nx, ny])
                visited[ny][nx] = True


while t > 0:
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    count = 0
    for x in range(m):
        for y in range(n):
            if not visited[y][x] and graph[y][x] == 1:
                bfs(graph, x, y, m, n, visited)
                count += 1
    print(count)
    t -= 1