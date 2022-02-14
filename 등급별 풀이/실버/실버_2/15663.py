from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = set()
for row in permutations(arr, M):
    result.add(row)

for r in sorted(result):
    print(*r)