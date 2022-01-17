import sys
input = sys.stdin.readline

n = int(input())
scores = [float(input()) for _ in range(n)]
scores.sort()

for i in range(7):
    print("{0:.3f}".format(scores[i]))