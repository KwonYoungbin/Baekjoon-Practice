def back(q, cnt):
    global result
    
    if cnt == M:
        result.add(tuple(q))
        return
        
    for val in arr:
        q.append(val)
        back(q, cnt+1)
        q.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = set()
back([], 0)

for row in sorted(result):
    print(*row)