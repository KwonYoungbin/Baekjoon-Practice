from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = set()
for r in combinations(arr, M):
    result.add(r)
    
for row in sorted(result):
    print(*row)