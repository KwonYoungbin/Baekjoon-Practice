import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)