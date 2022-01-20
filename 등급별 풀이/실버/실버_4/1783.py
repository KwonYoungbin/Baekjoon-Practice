# 다양한 조건을 모두 고려해야 함.

N, M = map(int, input().split())

cnt = 0
if N == 1:
    cnt = 1
elif N == 2:
    cnt = min(4, (M-1)//2 + 1)
elif M < 7:
    cnt = min(4, M)
else:
    cnt = M-2
print(cnt)