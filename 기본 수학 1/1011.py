import sys
import math

n = int(sys.stdin.readline())

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    dis = end - start
    move = round(math.sqrt(dis))
    if move**2 < dis:
        print((2*move))
    else:
        print((2*move) - 1)
                