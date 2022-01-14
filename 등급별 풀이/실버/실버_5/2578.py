def chk_bingo(graph):
    cnt = 0
    for row in graph:
        if row.count(0) == 5:
            cnt += 1
    
    for col in range(5):
        if graph[0][col] == graph[1][col] == graph[2][col] == graph[3][col] == graph[4][col] == 0:
            cnt += 1
    
    if graph[0][0] == graph[1][1] == graph[2][2] == graph[3][3] == graph[4][4] == 0:
        cnt += 1
    
    if graph[0][4] == graph[1][3] == graph[2][2] == graph[3][1] == graph[4][0] == 0:
        cnt += 1
        
    return cnt


bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))
    
number_list = []
for i in range(5):
    number_list += list(map(int, input().split()))

for idx, val in enumerate(number_list):
    finded = False
    for x in range(5):
        for y in range(5):
            if bingo[x][y] == val:
                bingo[x][y] = 0
                finded = True
                break
        
        if finded:
            break
    
    cnt = chk_bingo(bingo)
    if cnt >= 3:
        print(idx+1)
        break