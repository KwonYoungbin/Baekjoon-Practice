import sys

#이런 유형의 문제 가끔 나오니 기억해 둘 것
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, len(arr)):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])

print(min(arr[-1]))