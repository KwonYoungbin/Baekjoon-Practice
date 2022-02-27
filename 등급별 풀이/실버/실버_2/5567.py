from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = 1
    
    while q:
        now = q.popleft()
        
        for nxt in graph[now]:
            if visited[nxt] == 0:
                visited[nxt] = visited[now]+1
                q.append(nxt)
    
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

bfs(1)
print(sum([1 for i in visited if 2 <= i <= 3]))