import sys
input = sys.stdin.readline

for _ in range(int(input())):
    pos = [list(map(int, input().split())) for _ in range(4)]
    pos.sort(key=lambda x:(x[0], x[1]))
    line1 = (pos[0][0]-pos[1][0])**2 + (pos[0][1]-pos[1][1])**2
    line2 = (pos[0][0]-pos[2][0])**2 + (pos[0][1]-pos[2][1])**2
    line3 = (pos[1][0]-pos[3][0])**2 + (pos[1][1]-pos[3][1])**2
    line4 = (pos[2][0]-pos[3][0])**2 + (pos[2][1]-pos[3][1])**2
    cross1 = (pos[0][0]-pos[3][0])**2 + (pos[0][1]-pos[3][1])**2
    cross2 = (pos[1][0]-pos[2][0])**2 + (pos[1][1]-pos[2][1])**2
    if line1 == line2 == line3 == line4 and cross1 == cross2:
        print(1)
    else:
        print(0)