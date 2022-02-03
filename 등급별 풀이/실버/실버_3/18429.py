from itertools import permutations

N, K = map(int, input().split())
kits = list(map(int, input().split()))
result = 0

for row in permutations(range(N), N):
    result += 1
    now = 0
    for idx in row:
        now += kits[idx]
        now -= K
        if now < 0:
            result -= 1
            break
print(result)