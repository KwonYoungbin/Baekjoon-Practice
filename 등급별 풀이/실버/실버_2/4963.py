from collections import deque
import sys
input = sys.stdin.readline

moves = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]


def bfs(graph, a, b, visited):
    q = deque([(a, b)])
    visited[a][b] = True
    
    while q:
        x, y = q.popleft()
        
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


while True:
    W, H = map(int, input().rstrip().split())
    if W == H == 0:
        break
    
    graph = [list(map(int, input().strip().split())) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    result = 0
    for x in range(H):
        for y in range(W):
            if graph[x][y] and not visited[x][y]:
                bfs(graph, x, y, visited)
                result += 1
    print(result)