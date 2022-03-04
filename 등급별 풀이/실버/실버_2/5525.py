N = int(input())
M = int(input())
S = input()
result = 0
idx = 0
chk = 0

while idx < M-1:
    if S[idx:idx+3] == 'IOI':
        idx += 2
        chk += 1
        if chk == N:
            result += 1
            chk -= 1
    else:
        idx += 1
        chk = 0
print(result)