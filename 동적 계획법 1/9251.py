A = input()
B = input()

LCS = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for x in range(len(A)):
    for y in range(len(B)):
        if A[x] == B[y]:
            LCS[x+1][y+1] = LCS[x][y] + 1
        else:
            LCS[x+1][y+1] = max(LCS[x][y+1], LCS[x+1][y])
# print(*LCS, sep='\n')
print(max(LCS[-1]))