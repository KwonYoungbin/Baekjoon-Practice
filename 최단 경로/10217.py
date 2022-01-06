import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, start, times, M):
    q = []
    times[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        time, now = heapq.heappop(q)
        
        if times[now] < time:
            continue
        
        for dest, c, t in graph[now]:
            cost = time + t
            if (cost < times[dest]) and (M-c >= 0):
                times[dest] = cost
                heapq.heappush(q, (cost, dest))
                M -= c
                

t = int(input())
for _ in range(t):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    
    for __ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    
    times = [INF]*(N+1)
    
    dijkstra(graph, 1, times, M)