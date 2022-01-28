n = int(input())
result = 0
while n > 0:
    idx = 0
    while 2**idx <= n:
        idx += 1
    result += 3**(idx-1)
    n -= 2**(idx-1)
print(result)