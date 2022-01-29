from collections import deque
import sys
input = sys.stdin.readline

left = deque(list(input().rstrip()))
right = deque([])

for _ in range(int(input())):
    command = input().rstrip().split()
    if command[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.popleft())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])
print(''.join(left+right))