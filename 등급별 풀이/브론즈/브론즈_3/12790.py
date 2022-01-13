t = int(input())

for _ in range(t):
    stats = list(map(int, input().split()))
    result = 0
    hp = stats[0] + stats[4]
    mp = stats[1] + stats[5]
    a = stats[2] + stats[6]
    s = stats[3] + stats[7]
    
    result += (1*hp) if hp >= 1 else 1
    result += (5*mp) if mp >= 1 else 5
    result += (2*a) if a >= 0 else 0
    result += (2*s)
    
    print(result)