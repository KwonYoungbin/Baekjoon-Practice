import re

n = int(input())
pattern = input().replace('*', '[a-z]*')
chk = re.compile(pattern)

for _ in range(n):
    now = input()
    matched = chk.match(now)
    if matched and matched.group() == now:
        print('DA')
    else:
        print('NE')