import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))
dp = [0, arr[0]]

for i in range(1, N):
    dp.append(dp[-1] + arr[i])

for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    print(dp[b] - dp[a-1])