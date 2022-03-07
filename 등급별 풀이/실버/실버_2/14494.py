N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]

for x in range(N):
    arr[x][0] = 1
    
for y in range(M):
    arr[0][y] = 1
    
for x in range(1, N):
    for y in range(1, M):
        arr[x][y] = (arr[x-1][y] + arr[x][y-1] + arr[x-1][y-1])%1000000007

print(arr[-1][-1])