arr = list(map(int, input().split()))
arr.sort()

print(max((arr[1]-arr[0]),(arr[2]-arr[1]))-1)