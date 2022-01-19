import sys
input = sys.stdin.readline

n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)

max_val = 0
for i in range(n):
    if max_val < (rope[i] * (i+1)):
        max_val = (rope[i] * (i+1))
print(max_val)