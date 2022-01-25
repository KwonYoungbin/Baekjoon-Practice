n = int(input())
arr = list(map(int, input().split()))
result = 0
total = sum(arr)

for val in arr:
    total -= val
    result += total*val
print(result)