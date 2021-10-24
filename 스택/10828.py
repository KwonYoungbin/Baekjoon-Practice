import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'top':
        print(stack[-1]) if stack else print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(1) if not stack else print(0)
    elif command[0] == 'pop':
        print(stack.pop()) if stack else print(-1)