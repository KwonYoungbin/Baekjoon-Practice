from collections import defaultdict

import sys
input = sys.stdin.readline

n = int(input())
start = [input().strip() for _ in range(n)]
finish = defaultdict(int)

for _ in range(n-1):
    finish[input().strip()] += 1

for s in start:
    if s not in finish or finish[s] <= 0:
        print(s)
        break
    else:
        finish[s] -= 1