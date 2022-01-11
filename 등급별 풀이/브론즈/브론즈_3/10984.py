t = int(input())

for _ in range(t):
    n = int(input())
    sum_c, sum_g = 0, 0
    for __ in range(n):
        c, g = map(float, input().split())
        sum_c += int(c)
        sum_g += (c*g)
    print(sum_c, round(sum_g/sum_c, 1))