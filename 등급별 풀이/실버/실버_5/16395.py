n, k = map(int, input().split())
pascal = [[0],[1]]

for i in range(2, n+1):
    row = []
    for j in range(i):
        if j == 0 or j == i-1:
            row.append(1)
        else:
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
    pascal.append(row)

print(pascal[n][k-1])