import sys
import heapq

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


testcase = int(sys.stdin.readline())
for _ in range(testcase):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    distance = [[INF]*(n+1) for _ in range(n+1)]
    
    for __ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
    
    dijkstra(graph, s, distance)
    dijkstra(graph, g, distance)
    dijkstra(graph, h, distance)
    
    result = []
    for ___ in range(t):
        dest = int(sys.stdin.readline())
        origin_min_path = distance[s][dest]
        gtoh_min_path = distance[s][g] + distance[g][h] + distance[h][dest]
        htog_min_path = distance[s][h] + distance[h][g] + distance[g][dest]
        if origin_min_path == min(gtoh_min_path, htog_min_path):
            result.append(dest)
    
    result.sort()
    print(*result, sep=' ')