N = int(input())
win = [-1, 1, 0, 1, 1]

for i in range(5, N+1):
    if 0 in (win[i-1], win[i-3], win[i-4]):
        win.append(1)
    else:
        win.append(0)
print('SK' if win[N] else 'CY')