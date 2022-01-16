h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]
result = [[-1]*w for _ in range(h)]

for x in range(h):
    for y in range(w):
        if arr[x][y] == 'c':
            result[x][y] = 0

for x in range(h):
    for y in range(1, w):
        if result[x][y] != 0 and result[x][y-1] >= 0:
            result[x][y] = result[x][y-1]+1

for row in result:
    print(*row)