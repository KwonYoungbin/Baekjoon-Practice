while True:
    n, k = map(int, input().split())
    if n == k == 0:
        break
    
    top = 1
    bottom = 1
    for t in range(n, n-min(k,n-k), -1):
        top *= t
        
    for b in range(1, min(k+1, n-k+1)):
        bottom *= b
    
    print(top//bottom)