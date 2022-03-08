N = int(input())
result = 1

for i in range(2,N+1):
    result *= i
    while result%10 == 0:
        result //= 10
    result %= 100000000000000000
print(str(result)[-5:])