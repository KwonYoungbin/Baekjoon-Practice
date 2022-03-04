from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

rows = []
for i in range(1, N+1):
    rows.append(combinations(arr,i))
    
result = int(1e9)
for row in rows:
    for line in row:
        sour, sweet = 1, 0
        for so, sw in line:
            sour *= so
            sweet += sw
        result = min(result, abs(sour-sweet))
print(result)