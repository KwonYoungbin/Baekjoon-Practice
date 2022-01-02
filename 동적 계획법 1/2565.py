n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])

dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))