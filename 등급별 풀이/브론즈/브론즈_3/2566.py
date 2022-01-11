max_val = 0
x, y = 0, 0

for i in range(1, 10):
    temp = list(map(int, input().split()))
    m = max(temp)
    if max_val < m:
        max_val = m
        x, y = i, temp.index(m)+1
print(max_val)
print(x, y)