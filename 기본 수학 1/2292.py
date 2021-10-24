n = int(input())

now = 1
count = 1
while n > now:
    now += (6*count)
    count += 1
print(count)