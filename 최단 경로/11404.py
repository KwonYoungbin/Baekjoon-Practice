import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    s, e, dist = map(int, input().split())
    graph[s][e] = min(graph[s][e], dist)
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for x in range(1, n+1):
    for y in range(1, n+1):
        if graph[x][y] == INF:
            graph[x][y] = 0
            
for row in graph[1:]:
    print(' '.join(map(str,row[1:])))