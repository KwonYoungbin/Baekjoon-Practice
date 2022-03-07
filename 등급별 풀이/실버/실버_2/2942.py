import math

R, G = map(int, input().split())
cd = math.gcd(R, G)
arr = set()

for i in range(1, int(cd**0.5)+1):
    if cd % i == 0:
        arr.add(i)
        arr.add(cd//i)
        
for val in arr:
    print(val, R//val, G//val)