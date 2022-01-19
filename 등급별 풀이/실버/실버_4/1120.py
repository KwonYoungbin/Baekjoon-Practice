def chk(l, r):
    cnt = 0
    for x, y in zip(l, r):
        if x != y:
            cnt += 1
    return cnt

A, B = input().split()

if len(A) == len(B):
    print(chk(A, B))

else:
    gap = len(B) - len(A)
    min_miss_cnt = 50
    for i in range(gap+1):
        min_miss_cnt = min(min_miss_cnt, chk(A, B[i:i+len(A)]))
    print(min_miss_cnt)