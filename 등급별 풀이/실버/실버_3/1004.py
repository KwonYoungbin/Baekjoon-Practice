import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    n = int(input())
    cnt = 0
    for __ in range(n):
        nx, ny, r = map(int, input().rstrip().split())
        d1 = ((nx-x1)**2 + (ny-y1)**2)**0.5
        d2 = ((nx-x2)**2 + (ny-y2)**2)**0.5
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            cnt += 1
    print(cnt)