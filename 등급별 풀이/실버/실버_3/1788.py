n = int(input())
fibo = [0, 1]

for i in range(2, abs(n)+1):
    fibo.append((fibo[i-2] + fibo[i-1]) % 1000000000)
if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(fibo[abs(n)])