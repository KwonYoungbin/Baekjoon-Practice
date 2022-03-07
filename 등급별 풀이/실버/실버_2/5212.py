moves = [(1,0),(-1,0),(0,1),(0,-1)]

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
result = [['.']*C for _ in range(R)]

for x in range(R):
    for y in range(C):
        if graph[x][y] == 'X':
            count = 0
            for move in moves:
                nx = x + move[0]
                ny = y + move[1]
                
                if nx < 0 or nx >= R or ny < 0 or ny >= C or graph[nx][ny] == '.':
                    count += 1
            if count < 3:
                result[x][y] = 'X'

x_start, x_end = 0, R-1
y_start, y_end = 0, C-1

for i in range(R):
    x_start = i
    if 'X' in result[i]:
        break
    
for i in range(R-1, -1, -1):
    x_end = i
    if 'X' in result[i]:
        break
    
for i in range(C):
    y_start = i
    flag = False
    for j in range(R):
        if result[j][i] == 'X':
            flag = True
            break
    if flag:
        break
    
for i in range(C-1, -1, -1):
    y_end = i
    flag = False
    for j in range(R):
        if result[j][i] == 'X':
            flag = True
            break
    if flag:
        break

print(x_start, x_end)
print(y_start, y_end)
    
for x in range(x_start, x_end+1):
    for y in range(y_start, y_end+1):
        print(result[x][y], end='')
    print()