A, P = map(int, input().split())

arr = [A]
while True:
    now = list(map(int,str(arr[-1])))
    cal = 0
    for val in now:
        cal += val**P
    
    if cal in arr:
        print(arr.index(cal))
        break
    else:
        arr.append(cal)