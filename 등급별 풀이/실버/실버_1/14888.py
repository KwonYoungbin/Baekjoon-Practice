from itertools import combinations
from os import sep

def back(now, idx, add, diff, mul, div):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val, now)
        min_val = min(min_val, now)
        return
    
    if add:
        back(now+arr[idx], idx+1, add-1, diff, mul, div)
    if diff:
        back(now-arr[idx], idx+1, add, diff-1, mul, div)
    if mul:
        back(now*arr[idx], idx+1, add, diff, mul-1, div)
    if div:
        back(int(now/arr[idx]), idx+1, add, diff, mul, div-1)

N = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_val, min_val = -int(1e9), int(1e9)
back(arr[0], 1, oper[0], oper[1], oper[2], oper[3])
print(max_val, min_val, sep='\n')