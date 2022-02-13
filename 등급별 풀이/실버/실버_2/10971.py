def back(start, nxt, total, visited):
    global result
    
    if len(visited) == N:
        if graph[nxt][start] != 0:
            result = min(result, total+graph[nxt][start])
        return
    
    for i in range(N):
        if graph[nxt][i] != 0 and i not in visited and total < result:
            visited.append(i)
            back(start, i, total+graph[nxt][i], visited)
            visited.pop()


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = int(1e9)

for i in range(N):
    back(i, i, 0, [i])

print(result)