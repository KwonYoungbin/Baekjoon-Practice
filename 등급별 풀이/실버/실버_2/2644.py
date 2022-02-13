from collections import deque

def bfs(start, destination):
    q = deque([(start, 0)])
    visited[start] = True
    
    while q:
        now, dist = q.popleft()
        
        if now == destination:
            return dist
        
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, dist+1))
    return -1
        

N = int(input())
P1, P2 = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)
    
result = bfs(P1, P2)
print(result)