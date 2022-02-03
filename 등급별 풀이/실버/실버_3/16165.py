from collections import defaultdict

N, M = map(int, input().split())
teams = defaultdict(list)
mtot = defaultdict()

for _ in range(N):
    team = input()
    for __ in range(int(input())):
        member = input()
        teams[team].append(member)
        mtot[member] = team

for key in teams.keys():
    teams[key].sort()
            
for _ in range(M):
    name = input()
    kinds = int(input())
    if kinds == 1:
        print(mtot[name])
    else:
        print(*teams[name], sep='\n')
    