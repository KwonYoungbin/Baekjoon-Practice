def get_prime(num):
    for i in range(2, int(num**(0.5))+1):
        if num % i == 0:
            return False
    return True

n = int(input())
primes = []

for i in range(2, 104):
    if get_prime(i):
        primes.append(i)

for idx in range(1, len(primes)):
    if primes[idx]*primes[idx-1] > n:
        print(primes[idx]*primes[idx-1])
        break