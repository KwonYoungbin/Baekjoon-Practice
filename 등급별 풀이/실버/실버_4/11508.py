import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

total = 0
for i in range(0, n, 3):
    if i+2 > n-1:
        total += sum(arr[i:])
    else:
        total += arr[i] + arr[i+1]
print(total)