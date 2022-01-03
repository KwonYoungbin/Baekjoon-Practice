x = []
y = []
for _ in range(3):
    nx, ny = map(int, input().split())
    x.append(nx)
    y.append(ny)

r_x, r_y = 0, 0
for i in x:
    if x.count(i) == 1:
        r_x = i
        break
    
for i in y:
    if y.count(i) == 1:
        r_y = i
        break
print(r_x, r_y)