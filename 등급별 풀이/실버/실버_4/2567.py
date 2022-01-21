moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

paper = [[0]*101 for _ in range(101)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for r in range(x, x+10):
        for c in range(y, y+10):
            paper[r][c] = 1

result = 0            
for x in range(1, 101):
    for y in range(1, 101):
        if paper[x][y] == 1:
            cnt = 0
            for move in moves:
                nx = x + move[0]
                ny = y + move[1]
                if paper[nx][ny] == 1:
                    cnt += 1
                    
            if cnt == 3:
                result += 1
            elif cnt == 2:
                result += 2
print(result)