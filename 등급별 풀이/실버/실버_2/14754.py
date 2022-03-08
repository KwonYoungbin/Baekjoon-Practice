N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

total = 0
for row in graph:
    total += sum(row)
    
max_idx = set()
for x in range(N):
    max_val = max(graph[x])
    for y in range(M):
        if graph[x][y] == max_val:
            max_idx.add((x, y))
            break

for y in range(M):
    max_val = 0
    for x in range(N):
        if graph[x][y] > graph[max_val][y]:
            max_val = x
    max_idx.add((max_val, y))

for x, y in max_idx:
    total -= graph[x][y]
    
print(total)