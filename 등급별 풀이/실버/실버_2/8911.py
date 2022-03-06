move = [(0,1), (-1,0), (0,-1), (1,0)]

for _ in range(int(input())):
    command = input()
    pos = [(0,0)]
    direction = 0
    
    for c in command:
        if c == 'L':
            direction = (direction+1)%4
        elif c == 'R':
            direction = (direction+3)%4
        elif c == 'F':
            nx = pos[-1][0] + move[direction][0]
            ny = pos[-1][1] + move[direction][1]
            pos.append((nx, ny))
        else:
            nx = pos[-1][0] - move[direction][0]
            ny = pos[-1][1] - move[direction][1]
            pos.append((nx, ny))
    x_sort = sorted(pos, key=lambda x:x[0])
    y_sort = sorted(pos, key=lambda x:x[1])
    x_size = x_sort[-1][0] - x_sort[0][0]
    y_size = y_sort[-1][1] - y_sort[0][1]
    print(x_size * y_size)