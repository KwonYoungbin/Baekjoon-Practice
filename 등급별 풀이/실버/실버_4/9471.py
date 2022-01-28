from collections import defaultdict

def cycle():
    x = 2
    while True:
        if fibo[x] == 0 and fibo[x-1] == 1:
            return x
        x += 1
        fibo[x] = (fibo[x-1] + fibo[x-2]) % M


for _ in range(int(input())):
    N, M = map(int, input().split())
    fibo = defaultdict(int)
    fibo[0] = 0
    fibo[1] = 1
    fibo[2] = 1
    
    print(N, cycle())