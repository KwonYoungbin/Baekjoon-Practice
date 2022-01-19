import sys
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    com = input().split()
    if com[0] == 'push':
        q.append(int(com[1]))
    elif com[0] == 'pop':
        print(q.pop(0) if q else -1)
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        print(1 if not q else 0)
    elif com[0] == 'front':
        print(q[0] if q else -1)
    elif com[0] == 'back':
        print(q[-1] if q else -1)