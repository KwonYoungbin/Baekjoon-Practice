arr = input().split('-')

for i in range(len(arr)):
    if '+' in arr[i]:
        adder = map(int,arr[i].split('+'))
        arr[i] = sum(adder)
    else:
        arr[i] = int(arr[i])

result = arr[0]
for i in range(1, len(arr)):
    result -= arr[i]

print(result)