from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    
    arr = arr[1:]
    for row in combinations(arr, 6):
        print(*row, sep=' ')
    print()