k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
lines.sort()

left = 0
right = lines[-1]
answer = 1

while left <= right:
    mid = (left + right) // 2
    if mid == 0:
        break
    
    count = 0
    
    for line in lines:
        count += (line // mid)
    
    if count >= n:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)