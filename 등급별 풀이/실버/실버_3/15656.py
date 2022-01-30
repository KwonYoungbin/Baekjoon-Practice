N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def backtracking(q):
    if len(q) == M:
        print(*q)
        return
    
    for i in arr:
        q.append(i)
        backtracking(q)
        q.pop()

backtracking([])