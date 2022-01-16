A, B, N = map(int, input().split())
Q = A//B
R = A%B

for _ in range(N):
    temp = R*10
    Q = temp // B
    R = temp % B
print(Q)