# 아직 완벽히 이해 안됨.

a, b, c = map(int, input().split())

def convert(a, b):
    if b == 1:
        return a % c
    
    temp = convert(a, b//2)
    if b % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c

print(convert(a, b))