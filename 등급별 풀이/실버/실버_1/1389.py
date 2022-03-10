N, M = map(int, input().split())
dist = [[int(1e9)]*N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0

for _ in range(M):
    s, e = map(int, input().split())
    dist[s-1][e-1] = 1
    dist[e-1][s-1] = 1
    
for k in range(N):
    for x in range(N):
        for y in range(N):
            dist[x][y] = min(dist[x][y], dist[x][k]+dist[k][y])
            
result = list(map(sum, dist))
min_val = min(result)
print(result.index(min_val)+1)