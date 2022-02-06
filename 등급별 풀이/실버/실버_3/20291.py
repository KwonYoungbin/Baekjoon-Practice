from collections import defaultdict
import sys
input = sys.stdin.readline

dic = defaultdict(int)

for _ in range(int(input())):
    n, t = input().rstrip().split('.')
    dic[t] += 1
dic = sorted(dic.items(), key=lambda x:x[0])

for t, cnt in dic:
    print(t,cnt)