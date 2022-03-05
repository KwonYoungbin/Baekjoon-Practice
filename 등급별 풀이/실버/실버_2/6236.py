import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
money = [int(input()) for _ in range(N)]
result = int(1e9)

left = max(money)
right = sum(money)

while left <= right:
    mid = (left+right)//2
    
    cnt = 1
    remain = mid
    for now in money:
        if remain < now:
            cnt += 1
            remain = mid
        remain -= now
    
    if cnt > M:
        left = mid + 1
    else:
        right = mid - 1
        result = mid
print(result)