import sys

def get_gcd(a, b):
    x, y = max(a,b), min(a,b)
    while y:
        x, y = y, x%y
    return x

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

for i in range(1, n):
    gcd = get_gcd(arr[0],arr[i])
    print("%d/%d"%(arr[0]//gcd, arr[i]//gcd))