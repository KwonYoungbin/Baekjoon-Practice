M, N = map(int, input().split())
command = [input().split() for _ in range(N)]
moves = [(0,1), (1,0), (0,-1), (-1,0)]
idx = 0
x, y = 0, 0

chk = True
for com, d in command:
    d = int(d)
    if com == 'MOVE':
        x += (moves[idx][0] * d)
        y += (moves[idx][1] * d)
    else:
        if d == 0:
            idx = (idx+1)%4
        else:
            idx = (idx+3)%4
            
    if 0 > x or x > M or 0 > y or y > M:
        chk = False
        break

if chk:
    print(y, x)
else:
    print(-1)