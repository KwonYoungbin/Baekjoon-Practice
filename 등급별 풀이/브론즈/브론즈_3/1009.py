t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    a %= 10
    
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        if b % 2 == 0:
            print((a**2) % 10)
        else:
            print(a)
    else:
        r = b % 4
        if r == 1:
            print(a)
        elif r == 2:
            print(a**2 % 10)
        elif r == 3:
            print(a**3 % 10)
        else:
            print(a**4 % 10)