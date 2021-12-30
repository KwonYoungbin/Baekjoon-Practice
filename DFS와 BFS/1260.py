from collections import deque

dfs_result = []
bfs_result = []

def dfs(graph, start, dfs_visited):
    dfs_result.append(start)
    dfs_visited[start] = True
    for i in graph[start]:
        if not dfs_visited[i]:
            dfs(graph, i, dfs_visited)
        
def bfs(graph, start, bfs_visited):
    q = deque([start])
    bfs_visited[start] = True
    while q:
        now = q.popleft()
        bfs_result.append(now)
        
        for i in graph[now]:
            if not bfs_visited[i]:
                q.append(i)
                bfs_visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(len(graph)):
    graph[i].sort()

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

dfs(graph, v, dfs_visited)
bfs(graph, v, bfs_visited)

print(' '.join(map(str,dfs_result)))
print(' '.join(map(str,bfs_result)))