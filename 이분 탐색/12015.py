# 아직 이해 못함.

n = int(input())
arr = list(map(int, input().split()))

cmp_list = [0]

for val in arr:
    if cmp_list[-1] < val:
        cmp_list.append(val)
    else:
        left = 0
        right = len(cmp_list)
        
        while left < right:
            mid = (left + right) // 2
            if cmp_list[mid] < val:
                left = mid + 1
            else:
                right = mid
        cmp_list[right] = val
print(len(cmp_list)-1)