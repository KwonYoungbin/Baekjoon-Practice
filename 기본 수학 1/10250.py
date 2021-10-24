import sys

n = int(sys.stdin.readline())

for i in range(n):
    floor, room, person = map(int, sys.stdin.readline().split())
    f = person % floor
    r = (person//floor) + 1
    if f == 0:
        f, r = floor, r-1
    print(f*100+r)
    