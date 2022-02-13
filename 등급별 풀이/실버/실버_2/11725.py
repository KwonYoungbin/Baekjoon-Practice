from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([1])
    visited[1] = True
    
    while q:
        now = q.popleft()
        
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                roots[nxt] = now


N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
roots = [0] * (N+1)

for _ in range(N-1):
    s, e = map(int, input().strip().split())
    graph[s].append(e)
    graph[e].append(s)

bfs()
print(*roots[2:], sep='\n')