import math

n = list(map(int, input()))
count = [0] * 10
result = 0

for val in n:
    count[val] += 1
    
count[6] += count.pop()
count[6] = math.ceil(count[6]/2)

print(max(count))