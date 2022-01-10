n = int(input())
result = list(map(int, input().split()))
scores = [0]

for val in result:
    if val == 0:
        scores.append(0)
    else:
        scores.append(scores[-1]+1)
print(sum(scores))