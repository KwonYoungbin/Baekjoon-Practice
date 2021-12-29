n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = []

def ninetree(x, y, N):
    now = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if now != arr[i][j]:
                new_n = N//3
                ninetree(x, y, new_n)
                ninetree(x, y+new_n, new_n)
                ninetree(x, y+(2*new_n), new_n)
                ninetree(x+new_n, y, new_n)
                ninetree(x+new_n, y+new_n, new_n)
                ninetree(x+new_n, y+(2*new_n), new_n)
                ninetree(x+(2*new_n), y, new_n)
                ninetree(x+(2*new_n), y+new_n, new_n)
                ninetree(x+(2*new_n), y+(2*new_n), new_n)
                return
            
    result.append(now)

ninetree(0, 0, n)  
print(result.count(-1))
print(result.count(0))
print(result.count(1))