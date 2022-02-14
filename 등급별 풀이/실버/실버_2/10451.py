from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(graph, visited, start):
    q = deque([start])
    visited[start] = True
    
    while q:
        now = q.popleft()
        
        if not visited[graph[now]]:
            visited[graph[now]] = True
            q.append(graph[now])

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().strip().split()))
    graph = defaultdict(int)
    visited = [False] * (N+1)
    result = 0
    
    for idx, val in enumerate(arr):
        graph[idx+1] = val
    
    for i in range(1, N+1):
        if not visited[i]:
            bfs(graph, visited, i)
            result += 1
    print(result)