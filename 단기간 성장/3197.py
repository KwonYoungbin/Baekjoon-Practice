from collections import deque

def bfs(graph, start_pos, end_pos, r, c, moves):
    q = deque([start_pos])
    visited = [[False]*c for _ in range(r)]
    visited[start_pos[0]][start_pos[1]] = True
    
    while q:
        x, y = q.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != 'X' and not visited[nx][ny]:
                if nx == end_pos[0] and ny == end_pos[1]:
                    return True
                visited[nx][ny] = True
                q.append((nx, ny))
    return False

r, c = map(int, input().split())                        # 시간 초과 코드
graph = []
swan = []
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(r):
    graph.append(list(input()))
    if 'L' in graph[_]:
        swan.append((_, graph[_].index('L')))

count = 0
while True:
    if bfs(graph, swan[0], swan[1], r, c, moves):
        break
    possible = [[True]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if graph[x][y] == 'X':
                for move in moves:
                    nx = x + move[0]
                    ny = y + move[1]

                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.' and possible[nx][ny]:
                        graph[x][y] = '.'
                        possible[x][y] = False
                        break
    count += 1
print(count)