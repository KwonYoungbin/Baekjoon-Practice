S = input()
n = int(input())
result = 0

for _ in range(n):
    ring = input()
    ring += ring
    if S in ring:
        result += 1
        
print(result)