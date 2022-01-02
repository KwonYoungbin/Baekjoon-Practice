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

n = int(input())
arr = list(map(int, input().split()))
result = 0

for val in arr:
    if chk_prime(val):
        result += 1
print(result)