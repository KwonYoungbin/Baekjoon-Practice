n, k = map(int, input().split())
bag = [[0]*(k+1) for _ in range(n+1)]
arr = [[0,0]]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1,n+1):
    for j in range(1, k+1):
        w = arr[i][0]
        v = arr[i][1]

        if j < w:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(v + bag[i-1][j-w], bag[i-1][j])
print(bag)