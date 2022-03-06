moves = [(1,0),(0,1),(-1,0),(0,-1)]

def dfs(total, flower_cnt):
    global result
    if flower_cnt == 3:
        result = min(result, total)
        return
    
    for x in range(1, N-1):
        for y in range(1, N-1):
            if not visited[x][y]:
                temp = graph[x][y]
                possible = True
                for move in moves:
                    nx = x + move[0]
                    ny = y + move[1]
                    if visited[nx][ny]:
                        possible = False
                        break
                    temp += graph[nx][ny]
                
                if possible:
                    visited[x][y] = visited[x+1][y] = visited[x-1][y] = visited[x][y-1] = visited[x][y+1] = True
                    dfs(total+temp, flower_cnt+1)
                    visited[x][y] = visited[x+1][y] = visited[x-1][y] = visited[x][y-1] = visited[x][y+1] = False

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
result = int(1e9)
dfs(0, 0)
print(result)