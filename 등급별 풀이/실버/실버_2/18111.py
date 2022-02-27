import sys
input = sys.stdin.readline

N, M, B = map(int, input().strip().split())
ground = [list(map(int, input().strip().split())) for _ in range(N)]

min_time, H = int(1e9), 0
min_height = min(map(min, ground))
max_height = max(map(max, ground))

for i in range(min_height, max_height+1):
    up, down = 0, 0
    for x in range(N):
        for y in range(M):
            now = ground[x][y]
            if now > i:
                down += (now - i)
            elif now < i:
                up += (i - now)
    inventory = B + down
    
    if inventory < up:
        continue
    
    timer = 2*down + up
    if timer <= min_time:
        min_time = timer
        H = i
        
print(min_time, H)