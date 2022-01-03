while True:
    lines = list(map(int, input().split()))
    lines.sort()
    x, y, z = lines
    if x == y == z == 0:
        break
    
    if x**2 + y**2 == z**2:
        print('right')
    else:
        print('wrong')