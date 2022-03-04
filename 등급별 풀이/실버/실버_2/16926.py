N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(min(N,M)//2):
    cycle_count = 2*(N-(2*i)) + 2*(M-(2*i)-2)
    move_count = R%cycle_count
    
    for _ in range(move_count):
        x, y = i, i
        temp = arr[x][y]
        
        for j in range(i+1, N-i): #좌측
            x = j
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev
            
        for j in range(i+1, M-i): #하단
            y = j
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev
            
        for j in range(i+1, N-i): #우측
            x = N-j-1
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev
            
        for j in range(i+1, M-i): #상단
            y = M-j-1
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev

for row in arr:
    print(*row)