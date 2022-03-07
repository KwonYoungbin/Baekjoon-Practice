K = int(input())

result = [0]
era = [False] * 10000001

for i in range(2, 10000001):
    if era[i] == False:
        for j in range(i+i, 10000001, i):
            era[j] = True
        result.append(i)
print(len(result))
print(result[K])