N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for x in range(N):
    for y in range(M):
        if x == y == 0:
            continue
        elif x == 0:
            graph[x][y] += graph[x][y-1]
        elif y == 0:
            graph[x][y] += graph[x-1][y]
        else:
            graph[x][y] += max(graph[x-1][y-1], graph[x-1][y], graph[x][y-1])

print(graph[-1][-1])