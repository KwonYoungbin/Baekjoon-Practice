n = int(input())

while True:
    val = int(input())
    if val == 0:
        break

    if val % n == 0:
        print('%d is a multiple of %d.' %(val, n))
    else:
        print('%d is NOT a multiple of %d.' %(val, n))