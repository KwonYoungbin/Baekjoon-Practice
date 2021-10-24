n = int(input())
arr = []
stack = []
result = []
oper = []
idx = 0

for _ in range(n):
    arr.append(int(input()))

for i in range(1, n+1):
    stack.append(i)
    oper.append('+')
    while stack and stack[-1] == arr[idx]:
        result.append(stack.pop())
        oper.append('-')
        idx += 1

if len(arr) == len(result):
    print(*oper, sep='\n')
else:
    print('NO')