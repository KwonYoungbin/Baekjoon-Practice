t = int(input())
for _ in range(t):
    c = int(input())
    print(c//25, (c%25)//10, ((c%25)%10)//5, (((c%25)%10)%5)//1)