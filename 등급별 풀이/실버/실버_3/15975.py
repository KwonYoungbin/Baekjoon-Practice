from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0])

dic = defaultdict(list)
for pos, color in arr:
    dic[color].append(pos)

result = 0
for k in dic.keys():
    l = len(dic[k])
    if l != 1:
        for i in range(len(dic[k])):
            if i == 0:
                result += (dic[k][i+1] - dic[k][i])
            elif i == len(dic[k])-1:
                result += (dic[k][i] - dic[k][i-1])
            else:
                result += min((dic[k][i] - dic[k][i-1]), (dic[k][i+1] - dic[k][i]))
print(result)