X, Y = map(int, input().split())
Z = (Y*100) // X

if Z >= 99:
    print(-1)
else:
    result = 0
    left = 0
    right = X
    while left <= right:
        mid = (left + right) // 2
        newZ = (Y+mid)*100//(X+mid)
        if newZ >= Z+1:
            result = mid
            right = mid - 1
        elif newZ < Z+1:
            left = mid + 1
    print(result)