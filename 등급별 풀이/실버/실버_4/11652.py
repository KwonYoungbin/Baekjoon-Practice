from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
counter = Counter(arr)
counter = sorted(counter.items(), key=lambda x:(-x[1], x[0]))
print(counter[0][0])