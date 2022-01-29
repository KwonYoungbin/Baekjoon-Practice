N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

left = 0
right = 1
cal = arr[0]
while left < N:
    if cal == M:
        result += 1
        cal -= arr[left]
        left += 1
    
    if cal < M and right == N:
        break
    elif cal < M:
        cal += arr[right]
        right += 1
    elif cal > M:
        cal -= arr[left]
        left += 1
print(result)