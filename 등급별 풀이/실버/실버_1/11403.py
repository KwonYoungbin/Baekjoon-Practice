N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for x in range(N):
        for y in range(N):
            if graph[x][k] and graph[k][y]:
                graph[x][y] = 1

for row in graph:
    print(*row)