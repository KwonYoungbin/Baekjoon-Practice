R, C, W = map(int, input().split())
pascal = [[1]]

for x in range(1, R+W-1):
    row = []
    for y in range(x+1):
        if y == 0 or y == x:
            row.append(1)
        else:
            row.append(pascal[x-1][y-1] + pascal[x-1][y])
    pascal.append(row)

result = 0
idx = 0
for i in range(R-1, R+W-1):
    for j in range(C-1, C+idx):
        result += pascal[i][j]
    idx += 1
print(result)