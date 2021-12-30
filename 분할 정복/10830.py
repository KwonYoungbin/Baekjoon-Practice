def matrix_mul(n, a_mat, b_mat):
    temp = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            for k in range(n):
                temp[row][col] += a_mat[row][k] * b_mat[k][col]
            temp[row][col] %= 1000
    
    return temp

n, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

squared = [A]
seperate_list = bin(b)[2:][::-1]

for _ in range(1, len(seperate_list)):
    squared.append(matrix_mul(n, squared[-1], squared[-1]))

# 단위 행렬
result = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

for idx, val in enumerate(seperate_list):
    if int(val) == 1:
        result = matrix_mul(n, result, squared[idx])
            
for r in result:
    print(' '.join(map(str, r)))