n, k = map(int, input().split())
sigma = k*(k+1)//2

if n < sigma:
    print(-1)
else:
    if (n-sigma)%k == 0:
        print(k-1)
    else:
        print(k)