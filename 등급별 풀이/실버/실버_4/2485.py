import math
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

gc = math.gcd(arr[1]-arr[0], arr[2]-arr[1])
for i in range(3, n):
    gc = math.gcd(gc, arr[i]-arr[i-1])

print(((arr[-1]-arr[0])//gc) + 1 - n)