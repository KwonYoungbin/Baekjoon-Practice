from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = [False] * len(graph)
    visited[start] = True
    while q:
        now = q.popleft()
        visited[now] = True
        
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    
    return visited.count(True)-1
        

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

print(bfs(graph, 1))