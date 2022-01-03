while True:
    n = int(input())
    if n == 0:
        break
    
    chk = [True]*((2*n)+1)
    chk[0] = False
    chk[1] = False
    
    for i in range(2, int((2*n)**(1/2))+1):
        if chk[i] == True:
            for j in range(i+i, (2*n)+1, i):
                chk[j] = False
    
    print(chk[n+1:].count(True))