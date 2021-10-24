n = int(input())

for i in range(n):
    result = 0
    score = 0
    for j in list(input()):
        if j == 'O':
            score += 1
            result += score
        else:
            score = 0
    print(result)