import sys
input = sys.stdin.readline

n = int(input())
stu = [list(input().strip().split()) for _ in range(n)]
stu.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in stu:
    print(s[0])