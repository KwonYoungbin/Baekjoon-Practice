n = int(input())
A = list(map(int, input().split()))
temp = sorted(A)

for v in A:
    print(temp.index(v), end=' ')
    temp[temp.index(v)] = -1