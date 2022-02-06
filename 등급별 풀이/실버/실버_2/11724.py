from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, visited, start):
    q = deque([start])
    visited[start] = True
    
    while q:
        now = q.popleft()
        
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    s, e = map(int, input().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)
    
result = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, visited, i)
        result += 1
print(result)