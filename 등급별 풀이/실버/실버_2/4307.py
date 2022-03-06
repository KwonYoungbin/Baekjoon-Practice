import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l, n = map(int, input().strip().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    mx, mn = 0, 0
    
    for val in arr:
        mx = max(mx, l-val, val)
        mn = max(mn, min(l-val, val))
    
    print(mn, mx)