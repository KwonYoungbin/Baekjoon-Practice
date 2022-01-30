from itertools import combinations

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for row in combinations(arr, M):
    print(*row)