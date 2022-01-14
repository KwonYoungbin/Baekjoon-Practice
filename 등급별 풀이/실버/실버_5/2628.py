W, H = map(int, input().split())
n = int(input())

rows = [0, H]
cols = [0, W]

for _ in range(n):
    com, pos = map(int, input().split())
    if com == 0:
        rows.append(pos)
    else:
        cols.append(pos)

rows.sort()
cols.sort()

max_r = 0
for i in range(1, len(rows)):
    max_r = max(rows[i]-rows[i-1], max_r)
    
max_c = 0
for i in range(1, len(cols)):
    max_c = max(cols[i]-cols[i-1], max_c)

print(max_r * max_c)