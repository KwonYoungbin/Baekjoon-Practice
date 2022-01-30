N = int(input())
result = 0
base = 9
for i in range(1, len(str(N))+1):
    now = min(N, base)
    result += (now * i)
    base *= 10
    N -= now
    
    if N == 0:
        break
print(result)