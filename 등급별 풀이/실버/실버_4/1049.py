import math

n, m = map(int, input().split())
pack = []
perone = []

for _ in range(m):
    pac, one = map(int, input().split())
    pack.append(pac)
    perone.append(one)
    
mpp = min(pack)
mpo = min(perone)

print(min(n*mpo, mpp*(n//6)+mpo*(n%6), mpp*(math.ceil(n/6))))