from collections import deque
import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
distance = [int(1e9)] * (N+1)
visited = [False] * (N+1)
result = []

for _ in range(M):
    s, e = map(int, input().strip().split())
    graph[s].append(e)
    
def dijkstra():
    q = []
    heapq.heappush(q, (0, X))
    distance[X] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for nxt in graph[now]:
            cost = dist + 1
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))

dijkstra()
if distance.count(K):
    print(*[i for i in range(N+1) if distance[i] == K], sep='\n')
else:
    print(-1)

# def bfs():
#     global result
    
#     q = deque([X])
#     distance[X] = 0
#     visited[X] = True
    
#     while q:
#         now = q.popleft()
#         for nxt in graph[now]:
#             if not visited[nxt]:
#                 visited[nxt] = True
#                 distance[nxt] = distance[now] + 1
#                 if distance[nxt] == K:
#                     result.append(nxt)
#                 q.append(nxt)

# bfs()
# if result:
#     result.sort()
#     print(*result, sep='\n')
# else:
#     print(-1)