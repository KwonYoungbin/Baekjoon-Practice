arr = []

for _ in range(7):
    val = int(input())
    if val % 2 == 1:
        arr.append(val)
        
if not arr:
    print(-1)
else:
    print(sum(arr), min(arr), sep='\n')