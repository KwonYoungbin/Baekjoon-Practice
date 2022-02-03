import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
flag = False

for i in range(2, N):
    if arr[i-2]+arr[i-1] > arr[i] and arr[i]+arr[i-2] > arr[i-1] and arr[i-1]+arr[i] > arr[i-2]:
        flag = True
        print(arr[i-2] + arr[i-1] + arr[i])
        break

if not flag:
    print(-1)