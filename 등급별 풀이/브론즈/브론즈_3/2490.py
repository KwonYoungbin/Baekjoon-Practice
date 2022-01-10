arr = [list(map(int, input().split())) for _ in range(3)]

for sub in arr:
    if sub.count(0) == 1:
        print('A')
    elif sub.count(0) == 2:
        print('B')
    elif sub.count(0) == 3:
        print('C')
    elif sub.count(0) == 4:
        print('D')
    else:
        print('E')