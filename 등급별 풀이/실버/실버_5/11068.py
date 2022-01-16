def chk(num, B):
    temp = []
    while num > 0:
        temp.append(num%B)
        num //= B
    
    return True if temp == temp[::-1] else False

t = int(input())

for _ in range(t):
    n = int(input())
    possible = False
    for B in range(2, 65):
        if chk(n, B):
            possible = True
    
    print(1 if possible else 0)