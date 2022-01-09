n = int(input())
if n == 0:
    print('divide by zero')
else:
    arr = list(map(int,input().split()))
    avg = round(sum(arr)/n, 2)
    expect = 0
    for val in arr:
        expect += val*(1/n)
    if expect == 0:
        print('divide by zero')
    else:
        print('{:.2f}'.format(avg/expect))