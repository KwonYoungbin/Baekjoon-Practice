C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print(0)
else:
    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    chairs = [[0]*C for _ in range(R)]
    x, y = 0, 0
    direction = 0
    
    for i in range(1, C*R+1):
        chairs[x][y] = i
        
        if i == K:
            print(y+1, x+1)
            break
        
        nx = x + moves[direction][0]
        ny = y + moves[direction][1]
        
        if 0 <= nx < R and 0 <= ny < C and chairs[nx][ny] == 0:
            x = nx
            y = ny
        else:
            direction += 1
            direction %= 4
            x += moves[direction][0]
            y += moves[direction][1]