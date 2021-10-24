import sys

n = int(sys.stdin.readline())

for i in range(n):
    stack = []
    flag = False
    line = input()
    for ps in line:
        if ps == '(':
            stack.append(ps)
        else:
            if not stack:
                flag = True
                break
            else:
                stack.pop()
    print('NO') if flag or stack else print('YES')
        