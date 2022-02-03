import sys, math
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
jewelry = [int(input()) for _ in range(M)]
counter = Counter(jewelry)

left = 1
right = max(jewelry)
result = int(1e9)
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    
    for key in counter.keys():
        cnt += (math.ceil(key/mid)*counter[key])
    
    if cnt > N:
        left = mid + 1
    else:
        result = min(result,mid)
        right = mid - 1
print(result)