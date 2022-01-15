n, l = map(int, input().split())
snacks = list(map(int, input().split()))
snacks.sort()

for snack in snacks:
    if snack > l:
        break
    elif snack <= l:
        l += 1
print(l)