R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
possible = True

for x in range(R):
    for y in range(C):
        if graph[x][y] == '.':
            graph[x][y] = 'D'
        
        elif graph[x][y] == 'W':
            moves = [(1,0), (-1,0), (0,1), (0,-1)]
            
            for move in moves:
                nx = x + move[0]
                ny = y + move[1]
                
                if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == 'S':
                    possible = False
                    break
    
    if not possible:
        break
    
if not possible:
    print(0)
else:
    print(1)
    for row in graph:
        print(''.join(row))