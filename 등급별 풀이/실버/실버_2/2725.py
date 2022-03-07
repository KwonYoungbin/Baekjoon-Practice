import sys, math
input = sys.stdin.readline

dp = [0, 3]

for i in range(2, 1001):
    count = 0
    for j in range(1, i):
        if math.gcd(i, j) == 1:
            count += 2
    dp.append(dp[-1]+count)
    

for _ in range(int(input())):
    print(dp[int(input())])