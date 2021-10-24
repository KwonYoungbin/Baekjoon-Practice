import sys
n = int(sys.stdin.readline())
line = 1

while n > line:
    n -= line
    line += 1
    
if line % 2 == 0:
    print('%d/%d'%(n, (line-n+1)))
else:
    print('%d/%d'%((line-n+1), n))