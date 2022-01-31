dp = [1,1,2,4]
for i in range(4, 70):
    dp.append(dp[-1]+dp[-2]+dp[-3]+dp[-4])
    
for _ in range(int(input())):
    print(dp[int(input())])