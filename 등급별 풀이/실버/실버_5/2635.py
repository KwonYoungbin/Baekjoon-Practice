n = int(input())
max_score = 0
result = []

for i in range(n+1):
    temp = [n, i]
    while temp[-2] >= temp[-1]:
        temp.append(temp[-2]-temp[-1])
    
    if len(temp) > max_score:
        result = temp[:]
        max_score = len(temp)

print(max_score)
print(*result)