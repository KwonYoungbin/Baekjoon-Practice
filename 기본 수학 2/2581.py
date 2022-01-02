def chk_prime(val):
    if val == 1:
        return False
    elif 2 <= val <= 3:
        return True
    else:
        for i in range(2, int(val**(1/2))+1):
            if val % i == 0:
                return False
        return True

m = int(input())
n = int(input())
result = []

for val in range(m, n+1):
    if chk_prime(val):
        result.append(val)

if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)