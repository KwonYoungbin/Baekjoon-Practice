from collections import deque

n, k = map(int, input().split())
arr = deque([i for i in range(1, n+1)])
result = []

while len(result) < n:
    for i in range(k):
        arr.append(arr.popleft())
    result.append(arr.pop())

print('<', end='')
print(*result, sep=', ', end='')
print('>')