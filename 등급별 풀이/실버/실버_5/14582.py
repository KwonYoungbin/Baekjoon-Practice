A = list(map(int, input().split()))
B = list(map(int, input().split()))
be_win = False
A_sum, B_sum = 0, 0
for i in range(9):
    A_sum += A[i]
    if A_sum > B_sum:
        be_win = True
        break
    B_sum += B[i]

print('Yes' if be_win else 'No')