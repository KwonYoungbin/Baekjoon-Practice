n = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr[0]*arr[-1]) if len(arr) >= 2 else print(arr[0]**2)