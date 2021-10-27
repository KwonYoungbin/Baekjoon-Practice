import sys

m = 21
#arr를 떠올리는 것이 어려웠음. 추가 이해 필요
arr = [[[0]*m for _ in range(m)] for _ in range(m)]

def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(20, 20, 20)

    if arr[a][b][c] != 0:
        return arr[a][b][c]
    
    if a < b < c:
        arr[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return arr[a][b][c]
    else:
        arr[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return arr[a][b][c]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print("w(%d, %d, %d) = %d" %(a,b,c,w(a,b,c)))

