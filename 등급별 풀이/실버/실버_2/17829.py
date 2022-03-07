N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

while N > 1:
    sub_arr = []
    for x in range(0, N, 2):
        temp = []
        for y in range(0, N, 2):
            arr = [graph[x][y], graph[x][y+1], graph[x+1][y], graph[x+1][y+1]]
            arr.sort()
            temp.append(arr[-2])
        sub_arr.append(temp)
    graph = sub_arr
    N //= 2
print(graph[0][0])