n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]
scores.sort(key= lambda x:x[2])

rank = []
nations = []
while len(rank) < 3:
    nat, num, score = scores.pop()
    if nations.count(nat) < 2:
        nations.append(nat)
        rank.append([nat, num])

for row in rank:
    print(*row)