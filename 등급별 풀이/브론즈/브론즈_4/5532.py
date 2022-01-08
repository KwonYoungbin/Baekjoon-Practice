L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

kor = A//C + 1 if A%C != 0 else A//C
math = B//D + 1 if B%D != 0 else B//D
print(L - max(kor, math))