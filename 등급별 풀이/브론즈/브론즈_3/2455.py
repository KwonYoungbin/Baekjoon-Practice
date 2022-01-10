arr = [list(map(int, input().split())) for _ in range(4)]

max_val = 0
now = 0

for _out, _in in arr:
    now -= _out
    now += _in
    max_val = max(max_val, now)
print(max_val)