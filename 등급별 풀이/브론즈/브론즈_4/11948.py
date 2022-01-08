scores = [int(input()) for _ in range(6)]
print(sum(scores) - min(scores[:4]) - min(scores[4:]))