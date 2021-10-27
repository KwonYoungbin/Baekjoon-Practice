import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, len(arr)):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j == len(arr[i])-1:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
print(max(arr[-1]))