from collections import deque

n, m = map(int,input().split())
pos = list(map(int, input().split()))

cnt = 0
dq = deque([i for i in range(1, n+1)])

for p in pos:
    center = len(dq)//2
    while dq[0] != p:
        if dq.index(p) <= center:
            dq.append(dq.popleft())
        else:
            dq.appendleft(dq.pop())
        cnt += 1
    dq.popleft()
print(cnt)