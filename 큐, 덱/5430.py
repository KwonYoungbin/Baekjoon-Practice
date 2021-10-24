from collections import deque
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    func = input().replace('RR','')
    length = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')

    r, front, back = 0, 0, 0

    for f in func:
        if f == 'R':
            r += 1
        else:
            if r%2 == 0:
                front += 1
            else:
                back += 1
    
    if front + back <= length:
        arr = arr[front:length-back]
        if r%2 == 0:
            print('['+','.join(arr)+']')
        else:
            print('['+','.join(arr[::-1])+']')
    else:
        print('error')