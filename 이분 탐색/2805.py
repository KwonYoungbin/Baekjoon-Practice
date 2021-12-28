from collections import Counter

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

counter = Counter(trees)

left = 0
right = trees[-1]
answer = 0
while left <= right:
    mid = (left + right) // 2
    extras = 0
    for key in counter.keys():
        if key > mid:
            extras += ((key-mid)*counter[key])
    
    if extras >= m:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
print(answer)