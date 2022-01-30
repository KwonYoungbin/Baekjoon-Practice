n, m = map(int, input().split())

top = 1
bottom = 1

for i in range(1, min(n-m, m)+1):
    bottom *= i
    
for i in range(n-min(n-m, m)+1, n+1):
    top *= i

print(top//bottom)