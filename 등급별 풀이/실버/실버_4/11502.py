def chk_prime(num):
    for i in range(2, int(num**(0.5))+1):
        if num % i == 0:
            return False
    return True

for _ in range(int(input())):
    K = int(input())
    
    finded = False
    prime = [i for i in range(2, K+1) if chk_prime(i)]
    for i in range(len(prime)):
        for j in range(len(prime)):
            for k in range(len(prime)):
                if prime[i] + prime[j] + prime[k] == K:
                    print(prime[i], prime[j], prime[k])
                    finded = True
                    break
            if finded:
                break
        if finded:
            break
    
    if not finded:
        print(0)