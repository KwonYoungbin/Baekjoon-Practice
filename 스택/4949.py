while True:
    stack = []
    line = input()
    if line == '.':
        break
        
    for alpha in line:
        if alpha == '(' or alpha == '[':
            stack.append(alpha)
        elif alpha == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(alpha)
                break
        elif alpha == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(alpha)
                break
    
    print('yes') if not stack else print('no')