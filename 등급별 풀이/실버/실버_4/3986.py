n = int(input())

cnt = 0
for _ in range(n):
    s = input()
    if len(s)%2 == 0:
        stack = []
        chk = True
        
        for val in s:
            if val not in stack or stack[-1] != val:
                stack.append(val)
            elif stack[-1] == val:
                stack.pop()
            
        if not stack:
            cnt += 1
print(cnt)