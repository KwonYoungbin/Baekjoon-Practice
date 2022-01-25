from collections import defaultdict

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])

dots = defaultdict(list)
for pos, color in arr:
    dots[color].append(pos)

result = 0
for key in dots.keys():
    for i in range(len(dots[key])):
        if i == 0:
            result += dots[key][i+1] - dots[key][i]
        elif i == len(dots[key])-1:
            result += dots[key][i] - dots[key][i-1]
        else:
            result += min(dots[key][i]-dots[key][i-1], dots[key][i+1] - dots[key][i])
print(result)