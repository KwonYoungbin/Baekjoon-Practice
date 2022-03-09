for _ in range(int(input())):
    N = int(input())
    sticker = [[0]+list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*(N+1) for _ in range(2)]
    dp[0][1] = sticker[0][1]
    dp[1][1] = sticker[1][1]
    
    for y in range(2, N+1):
        dp[0][y] = max(dp[1][y-1], dp[1][y-2]) + sticker[0][y]
        dp[1][y] = max(dp[0][y-1], dp[0][y-2]) + sticker[1][y]
    
    print(max(dp[0][-1], dp[1][-1]))