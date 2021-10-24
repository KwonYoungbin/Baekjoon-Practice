n, m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(input())
    
result = []
for i in range(n-7):
    for j in range(m-7):
        c1, c2 = 0, 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if arr[a][b] == 'W':
                        c1 += 1
                    else:
                        c2 += 1
                else:
                    if arr[a][b] == 'B':
                        c1 += 1
                    else:
                        c2 += 1
        result.append(c1)
        result.append(c2)
        
print(min(result))