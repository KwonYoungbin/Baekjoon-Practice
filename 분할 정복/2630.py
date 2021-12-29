n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = []

def quadtree(x, y, N):
    now = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if now != arr[i][j]:
                new_N = N//2
                quadtree(x, y, new_N)
                quadtree(x, y+new_N, new_N)
                quadtree(x+new_N, y, new_N)
                quadtree(x+new_N, y+new_N, new_N)
                return
    
    answer.append(now)

quadtree(0, 0, n)
print(answer.count(0))
print(answer.count(1))