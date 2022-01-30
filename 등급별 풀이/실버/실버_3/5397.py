from collections import deque

for _ in range(int(input())):
    S = input()
    left, right = deque(), deque()
    cursor = 0
    for s in S:
        if s == '<' and left:
            right.appendleft(left.pop())
        elif s == '>' and right:
            left.append(right.popleft())
        elif s == '-' and left:
            left.pop()
        elif s.isalnum():
            left.append(s)
    print(''.join(left+right))