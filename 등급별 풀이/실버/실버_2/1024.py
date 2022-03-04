from re import sub


N, L = map(int, input().split())
result = []

for i in range(L, 101):
    center = N//i
    gap = i//2
    if i%2 != 0:
        subarr = [num for num in range(center-gap, center+gap+1)]
        if sum(subarr) == N:
            result = subarr
            break
    else:
        #case 1
        subarr1 = [num for num in range(center-gap+1, center+gap+1)]
        if sum(subarr1) == N:
            result = subarr1
            break
        
        #case 2
        subarr2 = [num for num in range(center-gap, center+gap)]
        if sum(subarr2) == N:
            result = subarr2
            break

if result and result[0] >= 0:
    print(*result)
else:
    print(-1)