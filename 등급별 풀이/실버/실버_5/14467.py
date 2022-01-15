from collections import defaultdict

n = int(input())
dic = defaultdict(list)
result = 0

for _ in range(n):
    num, pos = map(int, input().split())
    dic[num].append(pos)

for key in dic.keys():
    if len(dic[key]) >= 2:
        for i in range(1, len(dic[key])):
            if dic[key][i] != dic[key][i-1]:
                result += 1
print(result)