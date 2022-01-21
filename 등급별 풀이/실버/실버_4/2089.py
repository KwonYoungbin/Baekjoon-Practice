n = int(input())
if n == 0:
    print(0)
else:
    result = []
    while n != 0:
        if n % -2 == 0:
            result.append('0')
            n //= -2
        else:
            result.append('1')
            n = n//-2 + 1
    print(''.join(result[::-1]))