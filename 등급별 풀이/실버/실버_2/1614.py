N = int(input())
COUNT = int(input())

if N == 1:
    print(8*COUNT)
elif N == 5:
    print(8*COUNT+4)
else:
    if COUNT%2 == 0:
        print(N+(8*(COUNT//2))-1)
    else:
        print(8*((COUNT//2)+1)-N+1)