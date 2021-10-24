#유클리드 호제법
def gcd(a,b):
    x, y = max(a,b), min(a,b)

    while y:
        x, y = y, x%y

    print(x)
    print((a*b) // x)


a, b = map(int,input().split())
gcd(a,b)