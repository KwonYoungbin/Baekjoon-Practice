import sys

def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

def nCk(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))

case = int(sys.stdin.readline())

for _ in range(case):
    n, m = map(int, sys.stdin.readline().split())
    print(nCk(m,n))