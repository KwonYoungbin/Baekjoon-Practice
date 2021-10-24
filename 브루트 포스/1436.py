n = int(input())
value = 666
count = 0

while True:
    if '666' in str(value):
        count += 1
        if count == n:
            print(value)
            break
    value += 1