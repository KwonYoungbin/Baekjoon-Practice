import math

A, B = map(int, input().split())
cd = math.gcd(A,B)
print(A*B//cd)