from collections import deque

moves = [(2,1), (2,-1), (1,2), (1,-2), (-1,2), (-1,-2), (-2,1), (-2, -1)]

def bfs(l, start_x, start_y, end_x, end_y, weight):
    q = deque([[start_x, start_y]])
    weight[start_x][start_y] = 1
    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            return weight[end_x][end_y]-1
        
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if 0 <= nx < l and 0 <= ny < l and weight[nx][ny] == 0:
                q.append([nx, ny])
                weight[nx][ny] = weight[x][y] + 1
            
T = int(input())
while T > 0:
    l = int(input())
    weight = [[0] * l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    
    print(bfs(l, start_x, start_y, end_x, end_y, weight))
    
    T -= 1