n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0] if arr[0] > 0 else 0

for i in range(1, n):
    if arr[i] + dp[i-1] > 0:
        dp[i] = arr[i]+dp[i-1]

result = max(dp)
print(result) if result > 0 else print(max(arr))