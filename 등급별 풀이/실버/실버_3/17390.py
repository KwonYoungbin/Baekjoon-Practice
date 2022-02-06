import sys
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
arr.sort()

dp = [0, arr[0]]

for i in range(2, N+1):
    dp.append(dp[-1]+arr[i-1])

for _ in range(Q):
    L, R = map(int, input().rstrip().split())
    print(dp[R] - dp[L-1])