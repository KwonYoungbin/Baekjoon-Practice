from collections import deque
import math

N, S = map(int, input().split())
arr = list(map(int, input().split()))

if N == 1:
    print(abs(arr[0] - S))
else:
    diff_list = deque([])
    for val in arr:
        diff_list.append(abs(val-S))
    now = diff_list.popleft()
    
    while diff_list:
        now = math.gcd(now, diff_list.popleft())
    
    print(now)