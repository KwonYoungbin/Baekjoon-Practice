import sys

n = int(sys.stdin.readline())

count = 0
while n >= 0:
    if n%5 == 0:
        count += n//5
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)