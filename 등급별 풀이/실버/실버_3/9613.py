from itertools import combinations
import math

for _ in range(int(input())):
    arr = list(map(int, input().split()))[1:]
    result = 0
    for a, b in combinations(arr, 2):
        result += math.gcd(a,b)
    print(result)