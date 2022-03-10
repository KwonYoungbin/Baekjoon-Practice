prime = [True] * (1000001)
prime[0] = prime[1] = False
for i in range(2, 1000001):
    if prime[i]:
        for j in range(i+i, 1000001, i):
            prime[j] = False

while True:
    N = int(input())
    if N == 0:
        break
    
    possible = False
    for i in range(2, (N//2)+1):
        if prime[i] and prime[N-i]:
            print('%d = %d + %d' %(N, i, N-i))
            possible = True
            break
    
    if not possible:
        print('Goldbach\'s conjecture is wrong.')