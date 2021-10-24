import sys
n = int(input())
arr = []

for i in range(n):
    x = int(sys.stdin.readline())
    arr.append(x)

print(*sorted(arr), end='\n')