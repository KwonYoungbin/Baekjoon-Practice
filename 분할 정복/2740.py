a_n, a_m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(a_n)]
b_m, b_k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(b_m)]

result = [[0]*b_k for _ in range(a_n)]

for row in range(a_n):
    for col in range(b_k):
        for r, c in zip(A[row], [y[col] for y in B]):
            result[row][col] += (r*c)

for r in result:
    print(' '.join(map(str,r)))