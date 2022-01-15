from itertools import combinations

n = int(input())
max_idx = 0
max_val = 0

for idx in range(1, n+1):
    arr = list(map(int, input().split()))
    now_max = 0
    for sub_arr in combinations(arr, 3):
        total = sum(sub_arr)%10
        if total > now_max:
            now_max = total
    
    if now_max >= max_val:
        max_idx = idx
        max_val = now_max
print(max_idx)