n = int(input())
arr = list(map(int, input().split()))
stack = []
now = 1
out = []

possible = True
for val in arr:
    if val == now:
        out.append(val)
        now += 1
    elif val < now:
        possible = False
    elif not stack or stack[-1] > val:
        stack.append(val)
    
    while stack and stack[-1] == now:
        out.append(stack.pop())
        now += 1
        
print('Nice' if len(out)==n else 'Sad')