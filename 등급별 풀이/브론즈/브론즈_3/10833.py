n = int(input())
result = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        result += b
    else:
        result += b%a
print(result)