n = int(input())
arr = [float(input()) for _ in range(n)]

dp = [arr[0]]
for i in range(1, n):
    dp.append(max(arr[i], arr[i]*dp[-1]))

print("{:.3f}".format(max(dp)))