from itertools import permutations

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for row in permutations(arr, M):
    print(' '.join(map(str,row)))