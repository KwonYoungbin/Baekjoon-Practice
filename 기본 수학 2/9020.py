def chk_prime(val):
    if val == 1:
        return False
    elif 2 <= val <= 3:
        return True
    else:
        for i in range(2, int(val**(0.5))+1):
            if val % i == 0:
                return False
        return True

t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(n//2, 0, -1):
        if chk_prime(i) and chk_prime(n-i):
            print(i, n-i)
            break