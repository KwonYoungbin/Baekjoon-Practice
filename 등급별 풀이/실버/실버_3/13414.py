from collections import defaultdict
import sys
input = sys.stdin.readline

K, L = map(int, input().rstrip().split())
dic = defaultdict(int)

for i in range(L):
    dic[input().rstrip()] = i
    
cnt = 0
for i in sorted(dic.items(), key=lambda x:x[1]):
    cnt += 1
    if cnt > K:
        break
    print(i[0])