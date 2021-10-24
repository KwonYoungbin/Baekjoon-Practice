import sys

while True:
    fir, sec = map(int,sys.stdin.readline().split())
    if fir == sec == 0:
        break

    if sec % fir == 0:
        print('factor')
    elif fir % sec == 0:
        print('multiple')
    else:
        print('neither')