n, m = map(int,input().split())
cards = list(map(int,input().split()))

_max = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            _sum = cards[i]+cards[j]+cards[k]
            if _sum <= m and _sum > _max:
                _max = _sum

print(_max)