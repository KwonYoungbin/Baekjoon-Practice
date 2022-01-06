import heapq
import sys

INF = int(1e9)

def dijkstra(graph, start, distance):
    q = []
    distance[start][start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[start][now] < dist:
            continue
        
        for d, pos in graph[now]:
            cost = dist + d
            if cost < distance[start][pos]:
                distance[start][pos] = cost
                heapq.heappush(q, (cost, pos))


n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    start, end, w = map(int, sys.stdin.readline().split())
    graph[start].append((w, end))
    graph[end].append((w, start))
    
v1, v2 = map(int, sys.stdin.readline().split())
distance = [[INF]*(n+1) for _ in range(n+1)]

dijkstra(graph, 1, distance)
dijkstra(graph, v1, distance)
dijkstra(graph, v2, distance)

v1_path = distance[1][v1]+distance[v1][v2]+distance[v2][n]
v2_path = distance[1][v2]+distance[v2][v1]+distance[v1][n]
print(min(v1_path, v2_path) if v1_path < INF or v2_path < INF else -1)