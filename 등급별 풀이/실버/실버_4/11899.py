S = input()
stack = []

for s in S:
    if s == ')' and stack and stack[-1] == '(':
        stack.pop()
    else:
        stack.append(s)
print(len(stack))