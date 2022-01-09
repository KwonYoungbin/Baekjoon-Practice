b1, b2 = map(int, input().split())
d1, d2 = map(int, input().split())
j1, j2 = map(int, input().split())

b = max(abs(b1-j1), abs(b2-j2))
d = abs(d1-j1)+abs(d2-j2)

if b > d:
    print('bessie')
elif b < d:
    print('daisy')
else:
    print('tie')