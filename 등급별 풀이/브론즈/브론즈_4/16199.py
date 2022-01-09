b_y, b_m, b_d = map(int, input().split())
y, m, d = map(int, input().split())

cal_y, cal_m, cal_d = y-b_y, m-b_m, d-b_d
if cal_y == 0:
    print(0)
else:
    if cal_m < 0 or (cal_m == 0 and cal_d < 0):
        print(cal_y-1)
    else:
        print(cal_y)
print(cal_y+1)
print(cal_y)