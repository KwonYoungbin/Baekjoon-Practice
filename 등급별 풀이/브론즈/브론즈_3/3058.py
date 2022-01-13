t = int(input())

for _ in range(t):
    temp = list(map(int, input().split()))
    result = []
    for val in temp:
        if val % 2 == 0:
            result.append(val)
    print(sum(result), min(result))