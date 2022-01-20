n = int(input())
scores = [int(input()) for _ in range(n)]
scores.reverse()

result = 0
for i in range(1, n):
    if scores[i] >= scores[i-1]:
        result += (scores[i] - scores[i-1] + 1)
        scores[i] = scores[i-1]-1
print(result)