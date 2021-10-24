num = input()
arr = []

for i in num:
    arr.append(int(i))

print(*sorted(arr, reverse=True), sep='')