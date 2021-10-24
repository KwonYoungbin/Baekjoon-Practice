n = int(input())
count = n

for i in range(n):
    arr = []
    prev = ''
    for j in input():
        if j not in arr:
            arr.append(j)
            prev = j
        else:
            if prev != j:
                count -= 1
                break
print(count)