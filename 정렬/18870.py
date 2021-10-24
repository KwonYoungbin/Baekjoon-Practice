import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

temp = sorted(list(set(arr)))
dict = {temp[i] : i for i in range(len(temp))}
for i in arr:
    print(dict[i], end=' ')