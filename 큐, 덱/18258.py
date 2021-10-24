from collections import deque
import sys

n = int(sys.stdin.readline())
stack = deque()

for _ in range(n):
    col = sys.stdin.readline().split()

    if col[0] == 'push':
        stack.append(int(col[1]))
    elif col[0] == 'pop':
        print(stack.popleft()) if stack else print(-1)
    elif col[0] == 'size':
        print(len(stack))
    elif col[0] == 'empty':
        print(1) if not stack else print(0)
    elif col[0] == 'front':
        print(stack[0]) if stack else print(-1)
    elif col[0] == 'back':
        print(stack[-1]) if stack else print(-1)