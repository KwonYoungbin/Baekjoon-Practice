from collections import deque

N = int(input())
ball = list(map(int, input().split()))
arr = deque([])

for idx, val in enumerate(ball):
    arr.append([idx+1, val])
  
result = []
while arr:
    idx, num = arr.popleft()
    result.append(idx)
    
    if arr:
        if num < 0:
            for _ in range(abs(num)):
                arr.appendleft(arr.pop())
        else:
            for _ in range(num-1):
                arr.append(arr.popleft())
print(*result)