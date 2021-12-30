def matrix_mul(a_mat, b_mat):
    temp = [[0]*2 for _ in range(2)]
    for row in range(2):
        for col in range(2):
            for k in range(2):
                temp[row][col] += a_mat[row][k] * b_mat[k][col]
            temp[row][col] %= 1000000007
    
    return temp

n = int(input())
d2b = bin(n)[2:][::-1]
squared = [[[1, 1],[1, 0]]]

for i in range(1, len(d2b)):
    squared.append(matrix_mul(squared[-1], squared[-1]))

# 단위 행렬
result = [[1,0],[0,1]]

for idx, val in enumerate(d2b):
    if int(val) == 1:
        result = matrix_mul(result, squared[idx])
        
print(result[0][1])