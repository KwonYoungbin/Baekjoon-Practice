from collections import deque

def bfs(start):
    q = deque([start])
    
    while q:
        now = q.popleft()
        
        for i in range(1, arr[now]+1):
            if now+i < N and not dp[now+i]:
                dp[now+i] = dp[now]+1
                q.append(now+i)

N = int(input())

if N == 1:
    print(0)
else:
    arr = list(map(int, input().split()))
    dp = [0] * N
    bfs(0)

    print(dp[-1] if dp[-1] != 0 else -1)