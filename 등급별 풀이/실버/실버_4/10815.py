n = int(input())
cards = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
cards.sort()

for val in arr:
    left = 0
    right = n-1
    find = False
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == val:
            find = True
            break
        elif cards[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    
    print(1 if find else 0, end=' ')
