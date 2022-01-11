n = int(input())
max_val = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        max_val = max(max_val, 10000 + (a*1000))
    elif a == b:
        max_val = max(max_val, 1000 + (a*100))
    elif b == c:
        max_val = max(max_val, 1000 + (b*100))
    elif c == a:
        max_val = max(max_val, 1000 + (c*100))
    else:
        max_val = max(max_val, max(a, b, c)*100)
print(max_val)    