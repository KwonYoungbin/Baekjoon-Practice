# 시간 초과
# n, b = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(n)]

# result = [A]

# for _ in range(b-1):
#     temp = [[0]*n for _ in range(n)]
#     for row in range(n):
#         for col in range(n):
#             for r, c in zip(result[-1][row], [y[col] for y in A]):
#                 temp[row][col] += (r*c)
#             temp[row][col] %= 1000
#     result.append(temp)

# for r in result[-1]:
#     print(' '.join(map(str, r)))