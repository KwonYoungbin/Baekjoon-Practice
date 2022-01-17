n, m = map(int, input().split())
picture = [[0]*100 for _ in range(100)]

for _ in range(n):
    l_x, l_y, r_x, r_y = map(int, input().split())
    
    for x in range(l_x-1, r_x):
        for y in range(l_y-1, r_y):
            picture[x][y] += 1
            
result = 0
for x in range(100):
    for y in range(100):
        if picture[x][y] > m:
            result += 1
print(result)