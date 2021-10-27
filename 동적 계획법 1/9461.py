import sys

n = int(sys.stdin.readline())
arr = [1,1,1,2,2]

for _ in range(n):
    num = int(sys.stdin.readline())
    for i in range(len(arr), num):
        arr.append(arr[i-1]+arr[i-5])
    print(arr[num-1])