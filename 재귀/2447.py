import sys

def stars(n):
    mat = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            mat.append(n[i % len(n)] + ' '*len(n)+n[i%len(n)])
        else:
            mat.append(n[i % len(n)] * 3)
    return mat

star = ['***','* *','***']
n = int(sys.stdin.readline())
cnt = 0

while n != 3:
    n = int(n/3)
    cnt += 1
    
for i in range(cnt):
    star = stars(star)
for i in star:
    print(i)