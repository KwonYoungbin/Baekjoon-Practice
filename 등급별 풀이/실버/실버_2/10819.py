from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

result = 0
for row in permutations(arr, N):
    temp = 0
    for i in range(1, len(row)):
        temp += abs(row[i] - row[i-1])
    if temp > result:
        result = temp
print(result)