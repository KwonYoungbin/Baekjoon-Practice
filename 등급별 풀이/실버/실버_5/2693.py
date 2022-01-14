t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])