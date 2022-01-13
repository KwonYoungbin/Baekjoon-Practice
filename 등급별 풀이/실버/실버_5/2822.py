from operator import index


scores = []
idxs = []
result = 0

for _ in range(8):
    scores.append(int(input()))
    
for i in range(5):
    now = max(scores)
    indexed = scores.index(now)
    result += now
    idxs.append(indexed+1)
    scores[indexed] = 0
    
print(result)
print(*sorted(idxs))