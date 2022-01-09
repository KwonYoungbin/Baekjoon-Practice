r, c, n = map(int, input().split())
a = r//n + 1 if r%n != 0 else r//n
b = c//n + 1 if c%n != 0 else c//n
print(a*b)