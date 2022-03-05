prime = [0]*1000001

for i in range(2, int(1000000**0.5)+1):
    if prime[i] == 0:
        for j in range(i+i, 1000001, i):
            prime[j] = 1

for _ in range(int(input())):
    now = int(input())
    count = 0
    
    for i in range(2, (now//2)+1):
        if prime[i] == 0 and prime[now-i] == 0:
            count += 1
    print(count)