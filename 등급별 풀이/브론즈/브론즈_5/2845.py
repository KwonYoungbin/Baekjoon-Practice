L, P = map(int, input().split())
arr = list(map(int, input().split()))

for val in arr:
    print(val - (L*P), end=' ')