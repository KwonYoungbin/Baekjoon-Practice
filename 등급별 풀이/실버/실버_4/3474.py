import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result = 0
    base = 5
    
    while base <= n:
        result += n//base
        base *= 5
    print(result)