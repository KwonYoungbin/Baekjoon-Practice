a, b, c = int(input()), int(input()), int(input())
cal = list(map(int,str(a*b*c)))

for i in range(10):
    print(cal.count(i))