import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    price = int(input())
    options = int(input())
    
    for __ in range(options):
        q, p = map(int, input().split())
        price += (q*p)
    print(price)