N, s, P = map(int, input().split())
if N == 0:
    print(1)
else:
    scores = list(map(int, input().split())) + [s]
    scores.sort(reverse=True)
    rank = [1]
    for i in range(1, N+1):
        if scores[i] == scores[i-1]:
            rank.append(rank[-1])
        else:
            rank.append(i+1)
    
    if scores.index(s) + scores.count(s) > P:
        print(-1)
    else:
        print(rank[scores.index(s)])