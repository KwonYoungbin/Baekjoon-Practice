arr = set(range(1,10001))
temp = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    temp.add(i)

for k in sorted(arr-temp):
    print(k)