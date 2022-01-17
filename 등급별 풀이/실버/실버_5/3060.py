for _ in range(int(input())):
    N = int(input())
    foods = list(map(int, input().split()))
    day = 1
    while sum(foods) <= N:
        day += 1
        rightshift = [foods[i] for i in range(-1, 5)]
        leftshift = [foods[i] for i in range(1, 6)]
        leftshift.append(foods[0])
        
        for i in range(6):
            foods[i] += foods[i] + rightshift[i] + leftshift[i]
    print(day)