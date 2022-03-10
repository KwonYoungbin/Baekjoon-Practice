def cal(M, N, x, y):
    while x <= M * N:
        if (x-y)%N == 0:
            return x
        x += M
    return -1

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    print(cal(M, N, x, y))