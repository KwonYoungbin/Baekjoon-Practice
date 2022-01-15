from itertools import permutations

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]

possible = set()

for a in permutations(cards, k):
    possible.add(int(''.join(map(str,a))))
    
print(len(possible))