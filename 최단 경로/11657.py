# Bellman-Ford 알고리즘 (possible 변수의 역할과 원리가 이해안됨.)

import sys
input = sys.stdin.readline

INF = int(1e9)
possible = True

def bellman_ford(graph, start, distance, n):
    global possible
    distance[start] = 0
    for repeat in range(n):
        for i in range(1, n+1):
            for w, dest in graph[i]:
                if distance[i] != INF and distance[dest] > distance[i] + w:
                    distance[dest] = distance[i] + w
                    if repeat == n-1:
                        possible = False

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    start, end, w = map(int, input().split())
    graph[start].append((w, end))
    
bellman_ford(graph, 1, distance, n)

if possible:
    for i in range(2, n+1):
        print(distance[i] if distance[i] != INF else -1)
else:
    print(-1)