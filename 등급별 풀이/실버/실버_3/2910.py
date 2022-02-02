from collections import Counter

N, C = map(int, input().split())
arr = list(map(int, input().split()))
counter = Counter(arr)
result = sorted(counter.items(), key=lambda x:x[1], reverse=True)
for val, cnt in result:
    print(' '.join(map(str, [val]*cnt)), end=' ')