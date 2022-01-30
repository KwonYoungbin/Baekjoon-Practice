import math

N, A, B = map(int, input().split())
match = 1

while True:
    next_A = math.ceil(A/2)
    next_B = math.ceil(B/2)
    if next_A == next_B:
        break
    else:
        A = next_A
        B = next_B
        match += 1
print(match)