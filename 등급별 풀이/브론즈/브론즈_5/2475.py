arr = list(map(int, input().split()))
result = 0
for val in arr:
    result += val**2
print(result%10)