from collections import deque

n = int(input())
stack = deque([i for i in range(1, n+1)])

while len(stack) > 1:
    stack.popleft()
    stack.append(stack.popleft())
print(stack[0])