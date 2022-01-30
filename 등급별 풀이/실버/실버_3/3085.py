def chk():
    result = 0
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if graph[i][j] == graph[i][j-1]:
                cnt += 1
            else:
               cnt = 1
            
            if cnt > result:
                result = cnt 
        
        cnt2 = 1
        for k in range(1, N):
            if graph[k][i] == graph[k-1][i]:
                cnt2 += 1
            else:
                cnt2 = 1
            
            if cnt2 > result:
                result = cnt2
        
    return result
                    
N = int(input())
graph = [list(input()) for _ in range(N)]
moves = [(1, 0), (0, 1)] # 아래, 오른쪽
result = 0

for x in range(N):
    for y in range(N):
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            
            if nx >= N or ny >= N:
                continue
            
            # Swap
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
            
            now_max = chk()
            result = max(result, now_max)
            
            # RE-Swap
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
            
print(result)