N = int(input())
fibo = [1, 1]
for i in range(2, N+1):
    fibo.append(fibo[i-2]+fibo[i-1]+1)
print(fibo[N]%1000000007)