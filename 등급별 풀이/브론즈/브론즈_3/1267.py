n = int(input())
times = list(map(int,input().split()))
Y = 0
M = 0

for time in times:
    Y += (((time//30) + 1) * 10)
    M += (((time//60) + 1) * 15)
    
if Y == M:
    print('Y','M',Y)
elif Y < M:
    print('Y', Y)
else:
    print('M', M)