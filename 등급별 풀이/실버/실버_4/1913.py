n = int(input())
val = int(input())
snail = [[0]*n for _ in range(n)]
x, y = 0, 0
moves = [(1,0),(0,1),(-1,0),(0,-1)] # 하 -> 우 -> 상 -> 좌
direction = 0
find_x, find_y = 0, 0
for i in range(n**2, 0, -1):
    snail[x][y] = i
    
    if i == val:
        find_x = x+1
        find_y = y+1
    
    nx = x + moves[direction][0]
    ny = y + moves[direction][1]
    if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0:
        x = nx
        y = ny
    else:
        direction += 1
        direction %= 4
        x += moves[direction][0]
        y += moves[direction][1]

for row in snail:
    print(*row)
print(find_x, find_y)        