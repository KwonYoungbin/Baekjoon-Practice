arr = list(map(int, input().split()))

while True:
    for i in range(1, 5):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            print(*arr)
    
    
    if arr == sorted(arr):
        break