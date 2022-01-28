N1, N2 = map(int, input().split())
g1 = input()
g2 = list(input())
T = int(input())

jump_g1 = [0] * N1
for i in range(N1):
    jump_g1[i] = max(T, jump_g1[i])
    T -= 1

for i in range(N1):
    if jump_g1[i] >= N2:
        g2.insert(N2, g1[i])
    else:
        g2.insert(jump_g1[i], g1[i])
print(''.join(g2))