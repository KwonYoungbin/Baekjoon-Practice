import sys
sys.setrecursionlimit(100000)

N = int(input())

def facto(k, t):
    if t == 1:
        return k
    k *= t
    while k%10 == 0:
        k //= 10
    k %= 100000
    return facto(k, t-1)

print(facto(1, N)%10)