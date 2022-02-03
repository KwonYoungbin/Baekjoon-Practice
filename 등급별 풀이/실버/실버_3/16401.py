M, N = map(int, input().split())
arr = list(map(int, input().split()))

left = 1
right = max(arr)
result = 0
while left <= right:
    mid = (left+right) // 2
    person = 0
    
    for v in arr:
        person += v//mid
        
    if person >= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)