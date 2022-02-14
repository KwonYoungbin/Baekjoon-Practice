from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = set()
for r in combinations_with_replacement(arr, M):
    result.add(r)
    
for row in sorted(result):
    print(*row)