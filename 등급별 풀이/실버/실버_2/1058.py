N = int(input())
graph = [list(input()) for _ in range(N)]
result = [[0]*N for _ in range(N)]

for x in range(N):
    for y in range(N):
        if graph[x][y] == 'Y':
            result[x][y] = 1

for x in range(N):
    for y in range(N):
        for k in range(N):
            if graph[x][y] == 'Y' and graph[y][k] == 'Y':
                result[x][k] = 1
                
max_val = 0
for row in result:
    temp = sum(row)
    if temp != 0:
        max_val = max(max_val, temp-1)

print(max_val)