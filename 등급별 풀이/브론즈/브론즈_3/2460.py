now = 0
max_cnt = 0

for _ in range(10):
    _out, _in = map(int, input().split())
    now -= _out
    now += _in
    max_cnt = max(max_cnt, now)
print(max_cnt)