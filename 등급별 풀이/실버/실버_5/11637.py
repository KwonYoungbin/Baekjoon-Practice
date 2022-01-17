import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    
    max_score = max(arr)
    max_idx = arr.index(max_score)+1
    total = sum(arr)
    
    if arr.count(max_score) > 1:
        print('no winner')
    elif max_score > total/2:
        print('majority winner %d' %(max_idx))
    else:
        print('minority winner %d' %(max_idx))