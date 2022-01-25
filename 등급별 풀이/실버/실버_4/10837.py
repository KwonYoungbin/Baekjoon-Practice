import sys
input = sys.stdin.readline

K = int(input())
C = int(input())

for _ in range(C):
    M, N = map(int, input().strip().split())
    gap = abs(M-N)
    r = K-max(M,N)
    if M == N:
        print(1)
    elif M > N:
        print(1 if gap-r <= 2 else 0)
    elif M < N:
        print(1 if gap-r <= 1 else 0)