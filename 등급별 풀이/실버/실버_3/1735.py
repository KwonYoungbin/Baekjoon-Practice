import math

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

nA, nB = A1*B2 + A2*B1, B1*B2
GCD = math.gcd(nA, nB)
print(nA//GCD, nB//GCD)