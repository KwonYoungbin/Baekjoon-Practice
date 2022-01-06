# 시간 초과로 인해 PyPy3로 동작...

import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]

for _ in range(e):
    start, end, dist = map(int, input().split())
    graph[start][end] = dist
    
for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

result = INF
for i in range(1, v+1):
    result = graph[i][i] if result > graph[i][i] else result
print(result if result < INF else -1)