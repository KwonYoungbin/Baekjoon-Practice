import sys

n = int(sys.stdin.readline())

for i in range(n):
    f, r = int(sys.stdin.readline()), int(sys.stdin.readline())
    arr = [i for i in range(1,r+1)]
    
    for j in range(f):
        for k in range(r):
            if k != 0:
                arr[k] += arr[k-1]
    print(arr[-1])