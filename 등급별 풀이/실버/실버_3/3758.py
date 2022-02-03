from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k, t, m = map(int, input().rstrip().split())
    dic = defaultdict()
    for team in range(1, n+1):
        dic[team] = [[0]*(k+1), 0, -1]
        
    for time in range(m):
        i, j, s = map(int, input().rstrip().split())
        if dic[i][0][j] != 0:
            dic[i][0][j] = max(dic[i][0][j], s)
        else:
            dic[i][0][j] = s
        dic[i][1] += 1
        dic[i][2] = time
    
    result = sorted(dic.items(), key=lambda x:(-sum(x[1][0]), x[1][1], x[1][2]))
    
    for idx in range(n):
        if result[idx][0] == t:
            print(idx+1)
            break