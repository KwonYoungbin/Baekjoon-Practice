a, b = map(int,input().split())
a, b = min(a,b), max(a,b)

if (b-a)%2 != 0:
    print((a+b)*((b-a+1)//2))
else:
    print(((a+b)*((b-a)//2)) + (a+b)//2)