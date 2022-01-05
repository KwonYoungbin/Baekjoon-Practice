# DFS와 DP를 결합한 문제로, 아직 완벽히 이해 X

def scale(weights, n, now, left, right, dp, set_arr):
    val = abs(left - right)
    set_arr.add(val)
    
    if now == n:
        return 0
    
    if dp[now][val] == 0:
        # 왼쪽 저울에 올릴 때
        scale(weights, n, now+1, left+weights[now], right, dp, set_arr)
        
        # 오른쪽 저울에 올릴 때
        scale(weights, n, now+1, left, right+weights[now], dp, set_arr)
        
        # 저울에 올리지 않을 때
        scale(weights, n, now+1, left, right, dp, set_arr)
        
        dp[now][val] = 1
    

n = int(input())
weights = list(map(int, input().split()))
chk_cnt = int(input())
chk_list = list(map(int, input().split()))
dp = [[0]*15001 for _ in range(n+1)]
set_arr = set()

scale(weights, n, 0, 0, 0, dp, set_arr)

for number in chk_list:
    print('Y', end=' ') if number in set_arr else print('N', end=' ')