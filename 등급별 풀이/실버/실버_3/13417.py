from collections import deque

for _ in range(int(input())):
    T = int(input())
    arr = list(input().split())
    q = deque()
    for s in arr:
        if not q:
            q.append(s)
        elif q[0] < s:
            q.append(s)
        else:
            q.appendleft(s)
    print(''.join(q))