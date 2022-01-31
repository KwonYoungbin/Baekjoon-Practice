N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
max_size = min(N, M)
result = 0

for x in range(N):
    for y in range(M):
        left_up = graph[x][y]
        now_size = 0
        for i in range(max_size):
            if 0 <= x+i < N and 0 <= y+i < M:
                right_up = graph[x][y+i]
                left_down = graph[x+i][y]
                right_down = graph[x+i][y+i]
                if left_up == right_up == left_down == right_down:
                    now_size = (i+1)**2
                if result < now_size:
                    result = now_size
            else:
                break
print(result)