n = int(input())
switch = [-1] + list(map(int, input().split()))
m = int(input())

for _ in range(m):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, n+1, num):
            switch[i] = 1 if switch[i] == 0 else 0
    elif sex == 2:
        switch[num] = 1 if switch[num] == 0 else 0
        left = num-1
        right = num+1
        while 0 < left <= n and 0 < right <= n:
            if switch[left] == switch[right]:
                switch[left] = 1 if switch[left] == 0 else 0
                switch[right] = 1 if switch[right] == 0 else 0
                left -= 1
                right += 1
            else:
                break

for i in range(1, n+1):
    print(switch[i], end=' ')
    if i%20 == 0:
        print()