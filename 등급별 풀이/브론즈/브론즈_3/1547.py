m = int(input())
now = 1

for _ in range(m):
    a, b = map(int, input().split())
    if a == now:
        now = b
    elif b == now:
        now = a
print(now)