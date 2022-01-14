n = int(input())
people = []

for _ in range(n):
    people.append(list(input().split()))
    
people.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1])))
print(people[-1][0], people[0][0], sep='\n')