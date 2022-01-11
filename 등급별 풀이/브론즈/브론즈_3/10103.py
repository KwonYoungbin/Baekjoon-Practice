n = int(input())
a, b = 100, 100

for _ in range(n):
    left, right = map(int, input().split())
    if left > right:
        b -= left
    elif left < right:
        a -= right
print(a, b, sep='\n')