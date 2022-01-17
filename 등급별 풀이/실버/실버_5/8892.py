from itertools import combinations

for _ in range(int(input())):
    k = int(input())
    arr = [input() for _ in range(k)]
    chk = False
    
    for now in combinations(arr, 2):
        origin = ''.join(now)
        if origin == origin[::-1]:
            print(origin)
            chk = True
            break
        
        re_origin = ''.join(now[::-1])
        if re_origin == re_origin[::-1]:
            print(re_origin)
            chk = True
            break
    
    if not chk:
        print(0)