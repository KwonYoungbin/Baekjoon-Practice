n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort()

left = 1
right = homes[-1] - homes[0]
answer = 0
while left <= right:
    mid = (left + right) // 2
    now = 0
    count = 0
    
    for home in homes:
        if now == 0 or home >= now + mid:
            now = home
            count += 1
            
    if count >= c:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
print(answer)
    