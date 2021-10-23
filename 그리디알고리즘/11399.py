import sys

n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.sort()
result = 0

for i in range(n):
    result += time[i] * (n-i)
print(result)