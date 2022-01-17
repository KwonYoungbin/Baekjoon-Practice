string = input()
stack = []
result = 0

for s in string:
    if s not in stack:
        stack.append(s)
    elif stack[-1] == s:
        stack.pop()
    else:
        result += (len(stack) - stack.index(s) - 1)
        stack.remove(s)
print(result)