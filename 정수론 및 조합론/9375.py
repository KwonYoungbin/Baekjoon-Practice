import sys

case = int(sys.stdin.readline())

for _ in range(case):
    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        item, category = sys.stdin.readline().split()
        if category in dic:
            dic[category] += 1
        else:
            dic[category] = 1
    arr = list(dic.values())
    result = 1
    for num in arr:
        result *= (num+1)
    print(result-1)