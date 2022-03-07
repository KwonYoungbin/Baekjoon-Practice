N = int(input())

if N == 1:
    print('*')
else:
    w = 4*N - 3
    h = 4*N - 1
    
    result = [[' ']*w for _ in range(h)]
    
    def fill_star(n, x, y):
        if n == 1:
            result[y][x] = '*'
            result[y+1][x] = '*'
            result[y+2][x] = '*'
        else:
            for i in range(4*n-4):
                result[y][x] = '*'
                x -= 1
            for i in range(4*n-2):
                result[y][x] = '*'
                y += 1
            for i in range(4*n-4):
                result[y][x] = '*'
                x += 1
            for i in range(4*n-4):
                result[y][x] = '*'
                y -= 1
            result[y][x] = '*'
            result[y][x-1] = '*'
            fill_star(n-1, x-2, y)
    
    fill_star(N, w-1, 0)
    
    for row in result:
        print(''.join(row).rstrip())