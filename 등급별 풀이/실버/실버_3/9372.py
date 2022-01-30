from collections import defaultdict
import sys
input = sys.stdin.readline

def dfs(graph, start, visited, cnt):
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            cnt = dfs(graph, i, visited, cnt+1)
    return cnt

for _ in range(int(input())):
    N, M = map(int, input().rstrip().split())
    graph = defaultdict(list)
    visited = [False] * (N+1)
    for __ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
        
    result = dfs(graph, 1, visited, 0)
    print(result)