n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
answer = ""

def quadtree(x, y, N):
    now = arr[x][y]
    global answer 
    for i in range(x, x+N):
        for j in range(y, y+N):
            if now != arr[i][j]:
                new_n = N//2
                answer += "("
                quadtree(x, y, new_n)
                quadtree(x, y+new_n, new_n)
                quadtree(x+new_n, y, new_n)
                quadtree(x+new_n, y+new_n, new_n)
                answer += ")"
                return
    answer += str(now)
quadtree(0, 0, n)
print(answer)