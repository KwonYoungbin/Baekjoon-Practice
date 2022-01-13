A, B = map(int, input().split())
arr = []

for i in range(1, B+1):
    arr += [i]*i
    if len(arr) > 1000:
        break

print(sum(arr[A-1:B]))