n = int(input())
fibo = [0,1]

for _ in range(2, n+1):
    fibo.append((fibo[-2]+fibo[-1])%1000000007)
print(fibo[n])