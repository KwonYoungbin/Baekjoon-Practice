n = int(input())
arr = list(map(int, input().split()))
reverse_arr = arr[::-1]

inc_dp = [1] * n
dec_dp = [1] * n
    
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j]+1)
        if reverse_arr[j] < reverse_arr[i]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j]+1)
            
result = [0] * n
for i in range(n):
    result[i] = inc_dp[i] + dec_dp[n-i-1] - 1
    
print(max(result))