stones = [list(map(int, input().split())) for _ in range(19)]
moves = [(0,1), (1,0), (-1,1), (1,1)] # 우, 하, 우상, 우하

def chk(x, y):
    color = stones[x][y]
    for move in moves:
        nx = x + move[0]
        ny = y + move[1]
        cnt = 1
        
        while 0 <= nx < 19 and 0 <= ny < 19 and color == stones[nx][ny]:
            cnt += 1
            
            if cnt == 5:
                if 0 <= nx + move[0] < 19 and 0 <= ny + move[1] < 19 and color == stones[nx+move[0]][ny+move[1]]:
                    break
                if 0 <= x - move[0] < 19 and 0 <= y - move[1] < 19 and color == stones[x-move[0]][y-move[1]]:
                    break
                return True
            nx += move[0]
            ny += move[1]
        
    return False
        
find = False
for x in range(19):
    for y in range(19):
        if stones[x][y] != 0:
            if chk(x, y):
                print(stones[x][y])
                print(x+1, y+1)
                find = True
                break
    if find:
        break

if not find:
    print(0)