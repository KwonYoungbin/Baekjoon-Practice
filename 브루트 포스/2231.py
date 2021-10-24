n = int(input())

for i in range(1, n+1):
    temp = list(map(int,str(i)))
    if (i+sum(temp)) == n:
        print(i)
        break
    elif i == n:
        print(0)