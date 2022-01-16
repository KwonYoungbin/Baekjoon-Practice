x1, y1, x2, y2, x3, y3 = map(int, input().split())

if x1 == x2 == x3 or y1 == y2 == y3:
    print(-1.0)
elif (x2-x1 != 0 and y3-y1 == ((y2-y1)/(x2-x1))*(x3-x1)) or (x3-x1 != 0 and y2-y1 == ((y3-y1)/(x3-x1))*(x2-x1)):
    print(-1.0)
else:
    line1 = ((x2-x1)**2 + (y2-y1)**2)**(0.5)
    line2 = ((x3-x2)**2 + (y3-y2)**2)**(0.5)
    line3 = ((x1-x3)**2 + (y1-y3)**2)**(0.5)
    
    max_val = max((line1+line2)*2, (line2+line3)*2, (line1+line3)*2)
    min_val = min((line1+line2)*2, (line2+line3)*2, (line1+line3)*2)
    print(max_val - min_val)