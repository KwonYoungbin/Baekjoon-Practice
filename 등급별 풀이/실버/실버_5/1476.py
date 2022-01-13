E, S, M = map(int, input().split())

for i in range(1, 7981):
    e = i % 15 if i%15 != 0 else 15
    s = i % 28 if i%28 != 0 else 28
    m = i % 19 if i%19 != 0 else 19
    if e == E and s == S and m == M:
        print(i)
        break