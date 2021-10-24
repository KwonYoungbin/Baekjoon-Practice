import sys

#유클리드 호제법
def gcd(a,b):
    x,y = max(a,b), min(a,b)
    while y:
        x, y = y, x%y

    return (a*b) // x

n = int(sys.stdin.readline())

for _ in range(n):
    f, s = map(int,sys.stdin.readline().split())
    print(gcd(f,s))