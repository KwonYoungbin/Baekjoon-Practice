import sys
n = int(sys.stdin.readline())
arr = [0 for i in range(10000)]

for i in range(n):
    now = int(sys.stdin.readline())
    arr[now-1] += 1
    
for j in range(1,10001):
    for k in range(arr[j-1]):
        print(j)