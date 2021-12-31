from collections import deque

moves = [(0,1), (0,-1), (1,0), (-1,0)]

def cal_max(weights):
    result = 0
    for w in weights:
        result = max(result, max(w))
    return result-1

def non_zero(graph):
    for row in graph:
        if row.count(0) > 0:
            return False
    
    return True

def bfs(graph, pos, m, n, visited):
    q = deque(pos)
    
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

if non_zero(graph):
    print(0)
else:
    pos = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                pos.append([x, y])
                
    bfs(graph, pos, m, n, visited)
    
    if not non_zero(graph):
        print(-1)
    else:
        print(cal_max(graph))