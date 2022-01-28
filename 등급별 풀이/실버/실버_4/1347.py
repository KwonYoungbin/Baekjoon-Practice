n = int(input())
S = input()

moves = [(1,0), (0,-1), (-1,0), (0,1)] # 남, 서, 북, 동
dir = 0
pos = [(0,0)]

for s in S:
    if s == 'R':
        dir = (dir+1)%4
    elif s == 'L':
        dir = (dir+3)%4
    else:
        nx = pos[-1][0] + moves[dir][0]
        ny = pos[-1][1] + moves[dir][1]
        pos.append((nx, ny))

x_sorted = sorted(pos, key=lambda x:x[0])
y_sorted = sorted(pos, key=lambda x:x[1])
x_min, x_max = x_sorted[0][0], x_sorted[-1][0]
y_min, y_max = y_sorted[0][1], y_sorted[-1][1]

result = []
for x, y in pos:
    result.append((x-x_min, y-y_min))

graph = [['#']*(y_max-y_min+1) for _ in range(x_max-x_min+1)]
for x, y in result:
    graph[x][y] = '.'
    
for g in graph:
    print(''.join(g))