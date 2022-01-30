N = int(input())
arr = list(map(int, input().split()))

possible = False
for i in range(N-1, 0, -1):
    if arr[i-1] > arr[i]:
        idx = i-1
        possible = True
        break

if not possible:
    print(-1)
else:    
    for i in range(N-1, 0, -1):
        if arr[idx] > arr[i]:
            arr[idx], arr[i] = arr[i], arr[idx]
            arr = arr[:idx+1] + sorted(arr[idx+1:], reverse=True)
            print(*arr)
            break