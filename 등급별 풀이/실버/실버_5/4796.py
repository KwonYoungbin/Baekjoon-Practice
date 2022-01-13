idx = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    
    q = V//P
    r = V%P
    print('Case %d: %d' %(idx, L*q+min(L,r)))
    idx += 1