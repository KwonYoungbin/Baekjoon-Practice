import heapq
import sys

INF = int(1e9)

def dijkstra(graph, start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for d, pos in graph[now]:
            cost = dist + d
            if cost < distance[pos]:
                distance[pos] = cost
                heapq.heappush(q, (cost, pos))


v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    start, end, w = map(int, sys.stdin.readline().split())
    graph[start].append((w, end))
    
dijkstra(graph, k, distance)

for i in range(1, v+1):
    print(distance[i]) if distance[i] != INF else print('INF')