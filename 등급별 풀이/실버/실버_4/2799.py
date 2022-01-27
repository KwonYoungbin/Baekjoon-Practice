M, N = map(int, input().split())
graph = [input() for _ in range(5*M+1)]
result = [0] * 5

for i in range(M):
    for j in range(N):
        cnt = 0
        x = 1+(5*i)
        y = 1+(5*j)
        while graph[x][y] == '*':
            x += 1
            y += 1
            cnt += 1
        result[cnt] += 1

print(*result)