import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
arr = sorted(arr, key=lambda x:(x[1],x[0]))

starttime = 0
result = 0

for time in arr:
    if time[0] >= starttime:
        starttime = time[1]
        result += 1
print(result)