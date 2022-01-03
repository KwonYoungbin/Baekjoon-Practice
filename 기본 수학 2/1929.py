m, n = map(int, input().split())
chk = [True]*(n+1)
chk[0] = False
chk[1] = False

for i in range(2, int(n**(1/2))+1):
    if chk[i] == True:
        for j in range(i+i, n+1, i):
            chk[j] = False

for idx in range(m, n+1):
    if chk[idx]:
        print(idx)