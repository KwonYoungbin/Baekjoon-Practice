n = int(input())
moves = [(0,1), (0,-1), (1,0), (-1,0)]

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

result = [0]
groud_id = 1

def dfs(graph, x, y, n, visited, idx):
    visited[x][y] = True
    now_idx = idx
    if idx == 0:
        global groud_id
        now_idx = groud_id
        groud_id += 1
        result.append(1)
    else:
        result[idx] += 1
    
    for move in moves:
        nx = x + move[0]
        ny = y + move[1]
        
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(graph, nx, ny, n, visited, now_idx)
        
visited = [[False]*n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and not visited[x][y]:
            dfs(graph, x, y, n, visited, 0)

print(len(result)-1)
result.sort()
for i in range(1, len(result)):
    print(result[i])