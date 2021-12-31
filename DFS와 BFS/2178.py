from collections import deque

moves = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(graph, visited, n, m):
    q = deque([(1, [0, 0])])
    visited[0][0] = True
    
    while q:
        dist, now = q.popleft()
        x, y = now
        if x == n-1 and y == m-1:
            return dist
        
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((dist+1, [nx, ny]))
    

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
print(bfs(graph, visited, n, m))