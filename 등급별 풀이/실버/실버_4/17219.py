from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = defaultdict()

for _ in range(n):
    site, password = input().strip().split()
    dic[site] = password
    
for _ in range(m):
    print(dic[input().strip()])