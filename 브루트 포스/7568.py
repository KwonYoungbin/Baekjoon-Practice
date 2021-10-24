n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))
    
for j in range(n):
    rank = 1
    for k in range(n):
        if (arr[j][0] < arr[k][0]) and (arr[j][1] < arr[k][1]):
            rank += 1
    print(rank, end=' ')
            