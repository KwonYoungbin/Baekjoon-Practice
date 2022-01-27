N, L = map(int, input().split())
now = 1
time = 0

for _ in range(N):
    D, R, G = map(int, input().split())
    time += D-now
    now = D
    if time % (R+G) < R:
        time += (R - (time % (R+G)))
        
time += (L-now)
print(time)