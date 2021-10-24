h, m = map(int,input().split())

if m >= 45:
    print("%d %d"%(h,m-45))
else:
    if h == 0:
        print("23 %d"%(m+15))
    else:
        print("%d %d"%(h-1,m+15))