arr = [list(map(int, input().split())) for _ in range(3)]

for sub in arr:
    if sub.count(1) == 1:
        print('A')
    elif sub.count(1) == 2:
        print('B')
    elif sub.count(1) == 3:
        print('C')
    elif sub.count(1) == 4:
        print('D')
    else:
        print('E')