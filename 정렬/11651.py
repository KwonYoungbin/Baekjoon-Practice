import sys

n = int(input())
arr = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])
    
arr = sorted(arr, key=lambda x:(x[1], x[0]))
for i in arr:
    print("%d %d"%(i[0],i[1]))