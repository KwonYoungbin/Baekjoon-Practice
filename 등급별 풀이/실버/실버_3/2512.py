n = int(input())
arr = list(map(int, input().split()))
budget = int(input())

if sum(arr) <= budget:
    print(max(arr))
else:
    arr.sort()
    left, right = 0, arr[-1]
    min_gap = int(1e9)
    result = arr[0]
    while left <= right:
        mid = (left + right) // 2
        temp_total = 0
        for val in arr:
            temp_total += val if val <= mid else mid
        
        diff = budget-temp_total
        if diff < 0:
            right = mid - 1
        elif 0 <= diff < min_gap:
            min_gap = diff
            result = mid
            left = mid + 1
        elif diff > min_gap:
            left = mid + 1
    print(result)