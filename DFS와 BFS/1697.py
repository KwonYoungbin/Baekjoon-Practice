from collections import deque

def bfs(start, end, distance):
    q = deque([start])
    distance[start] = 0
    
    while q:
        now = q.popleft()
        if now == end:
            return distance[now]
        
        if 0 <= now-1 <= 100000 and distance[now-1] == 0:
            q.append(now-1)
            distance[now-1] = distance[now] + 1
            
        if 0 <= now+1 <= 100000 and distance[now+1] == 0:
            q.append(now+1)
            distance[now+1] = distance[now] + 1
            
        if 0 <= now*2 <= 100000 and distance[now*2] == 0:
            q.append(now*2)
            distance[now*2] = distance[now] + 1

n, k = map(int, input().split())
distance = [0] * 100001
print(bfs(n, k, distance))