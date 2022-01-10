import math
n, m, k = map(int, input().split())

g = n//2
b = m
team = min(g, b)
remain = (n-2*team) + (m-team) - k

if remain >= 0:
    print(team)
else:
    remain *= -1
    remain = math.ceil(remain/3)
    print(team-remain)