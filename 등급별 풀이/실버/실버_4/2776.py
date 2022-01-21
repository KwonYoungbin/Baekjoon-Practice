import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().strip().split()))
    A.sort()
    m = int(input())
    B = list(map(int, input().strip().split()))
    
    for num in B:
        left = 0
        right = n-1
        chk = 0
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == num:
                chk = 1
                break
            elif A[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        print(chk)