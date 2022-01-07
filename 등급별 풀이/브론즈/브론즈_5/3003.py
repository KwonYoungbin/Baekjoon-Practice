origin = [1, 1, 2, 2, 2, 8]
now = list(map(int, input().split()))

for a, b in zip(origin, now):
    print(a-b, end=' ')